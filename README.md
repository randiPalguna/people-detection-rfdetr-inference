## Environment Requirements
+ OS: Linux (mine using Ubuntu 24.04.4 LTS)
+ Python: 3.12 \
    To download python 3.12 (debian/ubuntu):
    ```
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.12
    sudo apt install python3.12-venv
    ```
+ NVIDIA CUDA: 12.x (tested with CUDA 12.2, you can check with `nvidia-smi`). If there is no NVIDIA driver, it will default to CPU executioner.
+ Git LFS: required to pull large .onnx model files from repository
    ```
    git lfs install
    ```

<br>

## Project Setup
1. Clone repository and enter project folder.
2. Install Git LFS and download model weights:
    ```
    git lfs pull
    ```
3. Install requirements.txt with:
    ```
    ./run.sh install or bash ./run.sh install
    ```
4. Run the model:
    ```
    ./run.sh run or bash ./run.sh run
    ```

<br>

## Configuration Files
+ Adjust runtime settings in `config.py`, including:
    + MODEL_PATH
    + CAMERA_SOURCE
    + INFERENCE_SIZE
    + CONFIDENCE_THRESHOLD
    + TRACKER
    + DISPLAY_WIDTH and DISPLAY_HEIGHT