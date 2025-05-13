# TrackedObjectArray.msg
# TrackedObject 여러 개를 포함하는 배열 메시지

std_msgs/Header header        # timestamp, frame_id (camera 또는 map 기준)
TrackedObject[] objects       # 객체 배열
