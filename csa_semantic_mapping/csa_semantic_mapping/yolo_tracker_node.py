import rclpy
from rclpy.node import Node
from csa_semantic_mapping.msg import TrackedObject, TrackedObjectArray

class YoloTrackerNode(Node):
    def __init__(self):
        super().__init__('yolo_tracker_node')
        self.publisher = self.create_publisher(TrackedObjectArray, '/tracked_objects', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        msg = TrackedObjectArray()
        # 실제 YOLO+StrongSORT 추론 결과를 여기로 넣음
        self.publisher.publish(msg)
        self.get_logger().info("Published /tracked_objects")

def main(args=None):
    rclpy.init(args=args)
    node = YoloTrackerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
