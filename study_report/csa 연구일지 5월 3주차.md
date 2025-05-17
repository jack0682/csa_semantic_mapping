CSA 연구 일지 – 2025-05-14
1. 오늘의 환경 및 작업 범위
연구 장소 및 상태: 자택 연구실 (고강도 집중 세션, 새벽 3시까지 지속)

실험 장비 사용 여부: Ryzen7 5800X + DDR4 32GB + RTX 3070 8GB

오늘 가능한 작업 유형: ROS2 노드 구조 변경 / 동기화 문제 해결 / 타입 디버깅 / 속도 조율 / 철학적 사유

---

2. 현재 진행중인 CSA 단계
 Stage 1: Semantic Mapping

 Stage 2: Self-Planning

 Stage 3: Explainable Control

 Stage 4: Multi-Robot Execution

 Stage 5: HRI & Common Ground

선택된 작업 단계:
Stage 1 — ROS2 기반 3D 시맨틱 추적 시스템의 실시간 동기화 안정성 검증

---

3. 오늘 수행한 작업 요약
 코드 구현: image_publisher_node, yolo_tracker_node 버퍼 및 구독자 동기화 로직 통합

 구조 설계: ament_cmake_python 구조를 ament_python으로 전환하여 setup.py 중심 구조로 정비

 에러 수정/디버깅: z must be of type float 오류의 근본 원인을 시간 동기화 문제로 재귀 추적

 실험 실행: 퍼블리셔 주기 조절 (30Hz → 10Hz → 1Hz), TimerAction 통한 지연 실행 실험

---
4. 주요 이슈 및 해결 내역

| 발생 일시 | 이슈 내용                                  | 대응 조치                                                  | 결과           |
| ----- | -------------------------------------- | ------------------------------------------------------ | ------------ |
| 05/12 | `ament_python` 전환 이후 `ros2 run` 실패     | `entry_points`, 디렉토리 구조 재조정                            | 해결           |
| 05/13 | 실행 가능하지만 `TrackedObject.z` float 오류 발생 | `float(z)`, `map(float, pos3d)` 적용, 실패 반복              | 미해결 → 원인 전환  |
| 05/13 | YOLO 추론보다 퍼블리셔 속도가 빠름                  | 퍼블리셔 `create_timer(0.1)` 조정 + `safe_depth_sample()` 도입 | 개선           |
| 05/14 | 버퍼 기반 동기화 로직 오작동                       | `match_and_process()` + `deque` 기반 완전 리팩토링             | 해결됨 (부분 안정화) |
| 05/14 | 퍼블리셔가 트래커보다 먼저 실행되어 프레임 유실             | `get_subscription_count()` 루프 + `TimerAction` 지연 실행 도입 | 해결됨          |

5. 기술적 통합 점검
 ament_python 전환 후 ros2 run 및 launch 구조 정상화

 TrackedObject.msg 타입 정의 및 pub/sub 정상 동작

 /camera/color/image_raw, /aligned_depth_to_color/image_raw 쌍으로 정확한 동기화 확인

 safe_depth_sample() 기반 깊이 샘플링 정확도 개선

 시맨틱 메모리 포맷 저장 및 Scene Graph 연결은 다음 단계로 이월


---

6. 철학적 반성 및 방향 확인
나는 지금, ROS2 내부 구조 변경과 시간 기반 메시지 동기화라는 **"기계적 질서"를 구현하려는 사고"**를 하고 있는가?

이 시스템은 단지 객체 위치를 추적하는 것이 아니라, "의미 있는 변화"를 기억하고 해석할 수 있는 실체가 되려 하고 있다.

실시간 동기화 실패 속에서도 내가 붙잡으려는 건 기계와 인간이 공유하는 시간성, 존재성, 주체성의 리듬이다.

---
 

7. 내일 또는 다음 작업 계획
 image_publisher_node → launch 지연 실행 (TimerAction) 방식 검증

 /tracked_objects 메시지를 받아 semantic_mapper.py에 전달하여 시맨틱 메모리 기록 시작

 JSON 기반 로그 자동 기록 시스템 구성

 Stage 2의 symbolic reasoning interface의 구조 설계 초안 마련





