import cv2
import time
import numpy as np
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from config import CAMERA_INDEX, YELLOW_TIME, N_FRAMES

class Camera:
    def __init__(self, index: int = CAMERA_INDEX):
        self.cap = cv2.VideoCapture(index)
        if not self.cap.isOpened():
            raise RuntimeError(f"Cannot open camera at index {index}")
        time.sleep(0.5)

    def capture_frames(self, n: int = N_FRAMES) -> list[np.ndarray]:
        interval = YELLOW_TIME / (n + 1)
        frames = []
        for _ in range(n):
            ret, frame = self.cap.read()
            if ret:
                frames.append(frame)
            time.sleep(interval)
        if not frames:
            raise RuntimeError("No frames captured")
        return frames

    def release(self):
        self.cap.release()