from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='csa_semantic_mapping', executable='yolo_tracker_node', name='yolo_tracker'),
        Node(package='csa_semantic_mapping', executable='slam_pose_node', name='slam_pose'),
        Node(package='csa_semantic_mapping', executable='semantic_mapper', name='semantic_mapper'),
        Node(package='csa_semantic_mapping', executable='rviz_visualizer', name='rviz_visualizer', output='screen'),
    ])
