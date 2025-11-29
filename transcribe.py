#!/usr/bin/env python3
"""Local video transcription using faster-whisper with Russian model."""

import subprocess
import sys
import time
from pathlib import Path


def check_ffmpeg() -> None:
    """Check if FFmpeg is installed."""
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            capture_output=True,
            check=True,
        )
    except FileNotFoundError:
        print("Error: FFmpeg not found. Install it with: brew install ffmpeg")
        sys.exit(1)


def extract_audio(video_path: Path) -> Path:
    """Extract audio from video to WAV format (16kHz, mono)."""
    audio_path = video_path.with_suffix(".wav")

    print("Extracting audio...")

    subprocess.run(
        [
            "ffmpeg",
            "-i", str(video_path),
            "-vn",
            "-acodec", "pcm_s16le",
            "-ar", "16000",
            "-ac", "1",
            "-y",
            str(audio_path),
        ],
        capture_output=True,
        check=True,
    )

    return audio_path


def transcribe_audio(audio_path: Path) -> str:
    """Transcribe audio file using faster-whisper."""
    from faster_whisper import WhisperModel

    print("Loading model... (first run will download ~3GB)")

    model = WhisperModel(
        "bzikst/faster-whisper-large-v3-russian",
        device="cpu",
        compute_type="float32",
    )

    print("Transcribing... (this may take a while)")

    segments, _ = model.transcribe(str(audio_path), language="ru")

    text_parts = []
    for segment in segments:
        text_parts.append(segment.text.strip())

    return " ".join(text_parts)


def main() -> None:
    """Main entry point."""
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <video_file>")
        sys.exit(1)

    video_path = Path(sys.argv[1])

    if not video_path.exists():
        print(f"Error: File not found: {video_path}")
        sys.exit(1)

    print(f"Processing: {video_path.name}")

    check_ffmpeg()

    start_time = time.time()

    try:
        audio_path = extract_audio(video_path)

        try:
            text = transcribe_audio(audio_path)

            output_path = video_path.with_suffix(".txt")
            output_path.write_text(text, encoding="utf-8")

            elapsed = time.time() - start_time
            print(f"Done! Saved to: {output_path}")
            print(f"Time elapsed: {elapsed:.1f}s")

        finally:
            if audio_path.exists():
                audio_path.unlink()

    except subprocess.CalledProcessError as e:
        print(f"Error: FFmpeg failed: {e.stderr.decode() if e.stderr else 'Unknown error'}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
