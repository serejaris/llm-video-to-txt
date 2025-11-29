#!/bin/bash

# Activate virtual environment and run transcription

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ -z "$1" ]; then
    echo "Usage: ./run.sh <video_file>"
    exit 1
fi

if [ ! -d "$SCRIPT_DIR/venv" ]; then
    echo "Virtual environment not found. Running setup..."
    bash "$SCRIPT_DIR/setup.sh"
fi

source "$SCRIPT_DIR/venv/bin/activate"
python3 "$SCRIPT_DIR/transcribe.py" "$1"
