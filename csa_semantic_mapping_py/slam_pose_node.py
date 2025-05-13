import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from builtin_interfaces.msg import Time
from std_msgs.msg import Header

from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy

import sys
import math
from tf_transformations import quaternion_from_euler  # or scipy.spatial.transform

class SlamPoseNode(Node):
    def __init__(self, test_mode=False):
        super().__init__('slam_pose_node')
        self.publisher_ = self.create_publisher(
            PoseStamped,
            '/camera/pose',
            QoSProfile(depth=10, reliability=ReliabilityPolicy.RELIABLE)
        )

        self.timer_ = self.create_timer(0.1, self.timer_callback)  # 10Hz
        self.test_mode = test_mode
        self.get_logger().info(f'SLAM Pose Node started (test_mode={self.test_mode})')

    def timer_callback(self):
        pose_msg = PoseStamped()
        pose_msg.header.stamp = self.get_clock().now().to_msg()
        pose_msg.header.frame_id = "map"  # or "odom", depending on SLAM output

        if self.test_mode:
            pose_msg.pose.position.x = 1.0
            pose_msg.pose.position.y = 2.0
            pose_msg.pose.position.z = 0.0

            q = quaternion_from_euler(0.0, 0.0, math.radians(45))
            pose_msg.pose.orientation.x = q[0]
            pose_msg.pose.orientation.y = q[1]
            pose_msg.pose.orientation.z = q[2]
            pose_msg.pose.orientation.w = q[3]

        else:
            # TODO: SLAM 연동 시 pose 데이터 업데이트
            pass

        self.publisher_.publish(pose_msg)

def main(args=None):
    rclpy.init(args=args)
    test_mode = '--test' in sys.argv
    node = SlamPoseNode(test_mode=test_mode)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
