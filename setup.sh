#!/bin/bash

# Setup virtual environment and install dependencies

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Use Python 3.10 (onnxruntime doesn't support 3.13 yet)
PYTHON="/opt/homebrew/bin/python3.10"

if [ ! -f "$PYTHON" ]; then
    echo "Error: Python 3.10 not found. Install with: brew install python@3.10"
    exit 1
fi

echo "Creating virtual environment with Python 3.10..."
"$PYTHON" -m venv "$SCRIPT_DIR/venv"

echo "Installing dependencies..."
source "$SCRIPT_DIR/venv/bin/activate"
pip install --upgrade pip
pip install -r "$SCRIPT_DIR/requirements.txt"

echo "Done! You can now use: scribe /path/to/video.mp4"
