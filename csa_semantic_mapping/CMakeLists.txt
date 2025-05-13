cmake_minimum_required(VERSION 3.10)
project(csa_semantic_mapping)

# ROS2 빌드 시스템 설정
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# 메시지 파일 지정
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/TrackedObject.msg"
  "msg/TrackedObjectArray.msg"
  DEPENDENCIES std_msgs geometry_msgs builtin_interfaces
)

# 파이썬 노드 설치 설정
ament_python_install_package(${PROJECT_NAME})

# 의존성 설정
ament_package()
