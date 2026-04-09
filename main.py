import torch
import cv2
from config import Config
from utils.camera import VideoStream
from core.model import ONNXRuntime
from core.tracker import Tracker
import time

def main():
    camera = VideoStream(Config.CAMERA_SOURCE, yt_livestream=Config.YT_LIVESTREAM)
    model = ONNXRuntime(
        model_path=Config.MODEL_PATH,
        inference_size=Config.INFERENCE_SIZE,
        conf_threshold=Config.CONFIDENCE_THRESHOLD,
        target_class_ids=Config.TARGET_CLASS_IDS,
    )
    tracker = Tracker(activate=Config.ACTIVATE_TRACKER, tracker=Config.TRACKER)
    display_size = (Config.DISPLAY_WIDTH, Config.DISPLAY_HEIGHT)

    while True:
        # time.sleep(0.05)
        frame = camera.read()
        if frame is None:
            break

        frame = cv2.resize(frame, display_size)

        detections = model.predict(frame, display_size)
        annotated_frame = tracker.track_and_draw(frame, detections)

        cv2.imshow('RF-DETR Test', annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()