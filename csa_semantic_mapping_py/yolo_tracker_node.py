import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Header
from cv_bridge import CvBridge

from csa_semantic_mapping_py.msg import TrackedObject, TrackedObjectArray
from .utils.yolov5_infer import YOLOv5Detector
from .utils.projection import deproject_pixel_to_point

import numpy as np
import cv2
from pathlib import Path
import sys

# boxmot 경로 등록
base_dir = Path(__file__).parent.parent.parent
boxmot_path = base_dir / 'models' / 'Yolov5_DeepSort_Pytorch' / 'boxmot'
sys.path.append(str(boxmot_path))

# boxmot 추적기 및 설정 임포트
from trackers.strongsort.strong_sort import StrongSORT
from utils.parser import get_config

class YOLOTrackerNode(Node):
    def __init__(self):
        super().__init__('yolo_tracker_node')

        # YOLO 초기화
        self.detector = YOLOv5Detector()

        # boxmot config 로딩
        cfg = get_config()
        cfg_path = boxmot_path / 'configs' / 'strongsort.yaml'
        cfg.merge_from_file(str(cfg_path))

        # StrongSORT 초기화
        reid_ckpt = base_dir / 'models' / 'weights' / 'osnet_x0_25_msmt17.pt'
        self.tracker = StrongSORT(
            model_path=str(reid_ckpt),
            max_dist=cfg.TRACKER.MAX_DIST,
            max_iou_distance=cfg.TRACKER.MAX_IOU_DISTANCE,
            max_age=cfg.TRACKER.MAX_AGE,
            n_init=cfg.TRACKER.N_INIT,
            nn_budget=cfg.TRACKER.NN_BUDGET,
            use_cuda=True
        )

        # ROS 통신 설정
        self.bridge = CvBridge()
        self.image_sub = self.create_subscription(Image, '/camera/color/image_raw', self.image_callback, 10)
        self.depth_sub = self.create_subscription(Image, '/camera/aligned_depth_to_color/image_raw', self.depth_callback, 10)
        self.pub = self.create_publisher(TrackedObjectArray, '/tracked_objects', 10)

        self.rgb_image = None
        self.depth_image = None

    def image_callback(self, msg):
        self.rgb_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        self.try_process(msg.header)

    def depth_callback(self, msg):
        self.depth_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        self.try_process(msg.header)

    def try_process(self, header: Header):
        if self.rgb_image is None or self.depth_image is None:
            return

        detections = self.detector.infer(self.rgb_image)
        if not detections:
            return

        bboxes_xyxy = []
        confidences = []
        class_ids = []

        for det in detections:
            bboxes_xyxy.append(det["bbox"])
            confidences.append(det["confidence"])
            class_ids.append(det["class_id"])

        # StrongSORT에 전달
        outputs = self.tracker.update(
            np.array(bboxes_xyxy),
            np.array(confidences),
            np.array(class_ids),
            self.rgb_image
        )

        tracked_objects = []
        for *bbox, track_id, class_id in outputs:
            x1, y1, x2, y2 = map(int, bbox)
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            depth = self.depth_image[cy, cx].astype(np.float32) / 1000.0
            pos3d = deproject_pixel_to_point(cx, cy, depth)
            if pos3d is None:
                continue

            obj = TrackedObject()
            obj.id = int(track_id)
            obj.class_id = int(class_id)
            obj.label = self.detector.class_name(class_id)
            obj.probability = float(confidences[class_ids.index(class_id)])
            obj.position.x, obj.position.y, obj.position.z = pos3d
            obj.header = header
            tracked_objects.append(obj)

        msg = TrackedObjectArray()
        msg.header = header
        msg.objects = tracked_objects
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = YOLOTrackerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
