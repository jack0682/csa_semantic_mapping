# yolov5_infer.py

import torch
import numpy as np
from .config import YOLO_CLASSES, CONFIDENCE_THRESHOLD

class YOLOv5Detector:
    def __init__(self, model_path='yolov5s.pt', device='cuda'):
        self.device = device if torch.cuda.is_available() else 'cpu'
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
        self.model.to(self.device).eval()

    def infer(self, image_np):
        results = self.model(image_np)
        detections = []

        for *xyxy, conf, cls in results.xyxy[0]:
            if conf < CONFIDENCE_THRESHOLD:
                continue
            class_id = int(cls.item())
            label = YOLO_CLASSES[class_id] if class_id < len(YOLO_CLASSES) else "unknown"
            x1, y1, x2, y2 = map(int, xyxy)
            detections.append({
                "bbox": [x1, y1, x2, y2],
                "label": label,
                "confidence": float(conf.item()),
                "class_id": class_id
            })
        return detections
