# config.py

YOLO_CLASSES = [
    "person", "cup", "keyboard", "mouse", "chair", "bottle", "book", "cell phone"
]

CLASS_COLOR_MAP = {
    "person": (255, 0, 0),
    "cup": (0, 255, 0),
    "keyboard": (0, 0, 255),
    "mouse": (255, 255, 0),
    "chair": (255, 0, 255),
    "bottle": (0, 255, 255),
    "book": (128, 128, 0),
    "cell phone": (0, 128, 128)
}

CONFIDENCE_THRESHOLD = 0.5
NMS_IOU_THRESHOLD = 0.4

# Camera intrinsics (example RealSense D435)
CAMERA_INTRINSICS = {
    "fx": 615.0,
    "fy": 615.0,
    "cx": 320.0,
    "cy": 240.0,
}
