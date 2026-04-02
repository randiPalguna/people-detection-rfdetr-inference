import os

class Config:
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

    # Inference configuration
    # MODEL_PATH = os.path.join(PROJECT_ROOT, "weights", "v1.sim.onnx")
    MODEL_PATH = os.path.join(PROJECT_ROOT, "weights", "v2.onnx")
    TARGET_CLASS_IDS = [1]
    CAMERA_SOURCE = "https://motchallenge.net/sequenceVideos/PETS09-S2L2-raw.webm"
    # CAMERA_SOURCE = 0
    YT_LIVESTREAM = False
    DISPLAY_WIDTH = 768
    DISPLAY_HEIGHT = 576


    # INFERENCE_SIZE = (384, 384) # for v1.sim.onnx model
    INFERENCE_SIZE = (672, 672) # for v2.onnx model
    CONFIDENCE_THRESHOLD = 0.05
    TRACKER = "OC-SORT"