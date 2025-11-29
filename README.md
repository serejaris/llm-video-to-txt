# Video Transcribe

Local video transcription using faster-whisper with Russian language model.

## Prerequisites

- Python 3.10+
- FFmpeg

```bash
brew install ffmpeg
```

## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python transcribe.py /path/to/video.mp4
```

Output will be saved as `/path/to/video.txt`.

## Notes

- First run downloads the model (~3GB)
- Model: `bzikst/faster-whisper-large-v3-russian` (CTranslate2 version of antony66/whisper-large-v3-russian)
- Uses CPU with float32 (faster-whisper doesn't support MPS)
- Requires Python 3.10-3.12 (onnxruntime doesn't support 3.13)
