# TrackedObject.msg
# 단일 객체의 시맨틱 정보 표현

int32 id                # Tracking ID (StrongSORT로부터 추출)
string label            # 객체의 클래스명 (YOLO 예: "person", "cup", ...)
float32 probability     # YOLO confidence score
geometry_msgs/Point position  # SLAM 기반 3D 위치 [x, y, z]
int32 class_id          # YOLO 클래스 ID (int형, 숫자 라벨)
std_msgs/Header header  # timestamp와 frame_id 포함
