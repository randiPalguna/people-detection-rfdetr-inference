#!/bin/bash
export PYTHONDONTWRITEBYTECODE=1 # no generating pycache files

set -e

COMMAND=$1

if [ "$COMMAND" == "install" ]; then
    echo "[INFO] Creating environment..."
    if [ ! -d ".venv" ]; then
        echo "[INFO] Creating virtual environment '.venv'..."
        python3.12 -m venv .venv
    else
        echo "[INFO] Virtual environment '.venv' already exists."
    fi

    echo "[INFO] Activating environment..."
    source .venv/bin/activate

    echo "[INFO] Installing dependencies from requirements.txt..."
    python3.12 -m pip install --upgrade pip -q
    pip install -r requirements.txt

    mkdir -p .venv/lib/python3.12/site-packages/cv2/qt/fonts
    
    echo "========================================"
    echo "[SUCCESS] Installation complete!"
    echo "You can now start the application by typing: ./run.sh run"
    echo "========================================"

elif [ "$COMMAND" == "run" ]; then
    if [ ! -d ".venv" ]; then
        echo "[ERROR] Virtual environment not found!"
        echo "Please run './run.sh install' first to set up the project."
        exit 1
    fi

    echo "[INFO] Activating virtual environment..."
    source .venv/bin/activate

    echo "[INFO] Executing..."
    echo "========================================"
    python3.12 main.py

else
    echo "Usage: ./run.sh [command]"
    echo ""
    echo "Commands:"
    echo "  install   Creates the virtual environment and installs Python dependencies."
    echo "  run       Activates the environment and starts the AI inference."
    echo ""
    echo "Example:"
    echo "  ./run.sh install"
    exit 1
fi