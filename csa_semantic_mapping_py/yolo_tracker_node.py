# yolo_tracker_node.py

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

# 추후 StrongSORT import도 연결 필요

class YOLOTrackerNode(Node):
    def __init__(self):
        super().__init__('yolo_tracker_node')

        # YOLO + StrongSORT 초기화
        self.detector = YOLOv5Detector()
        # self.tracker = StrongSORT(...)  # 나중에 구현

        # ROS 구독 및 퍼블리셔
        self.bridge = CvBridge()
        self.image_sub = self.create_subscription(Image, '/camera/color/image_raw', self.image_callback, 10)
        self.depth_sub = self.create_subscription(Image, '/camera/aligned_depth_to_color/image_raw', self.depth_callback, 10)

        self.pub = self.create_publisher(TrackedObjectArray, '/tracked_objects', 10)

        # 이미지 및 depth 버퍼
        self.rgb_image = None
        self.depth_image = None

    def image_callback(self, msg):
        self.rgb_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        self.process_if_ready(msg.header)

    def depth_callback(self, msg):
        self.depth_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        self.process_if_ready(msg.header)

    def process_if_ready(self, header: Header):
        if self.rgb_image is None or self.depth_image is None:
            return

        # 객체 탐지
        detections = self.detector.infer(self.rgb_image)

        # StrongSORT 추적은 나중에 연결 예정
        tracked_objects = []

        for det in detections:
            x1, y1, x2, y2 = det['bbox']
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            depth = self.depth_image[cy, cx].astype(np.float32) / 1000.0  # mm → m

            pos3d = deproject_pixel_to_point(cx, cy, depth)
            if pos3d is None:
                continue

            obj = TrackedObject()
            obj.id = -1  # 추후 tracker 결과로 대체
            obj.label = det['label']
            obj.probability = det['confidence']
            obj.position.x, obj.position.y, obj.position.z = pos3d
            obj.class_id = det['class_id']
            obj.header = header

            tracked_objects.append(obj)

        # 퍼블리시
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
