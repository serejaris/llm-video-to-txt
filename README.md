<!-- hq-readme-ru: 2026-05-09 -->
# llm-video-to-txt

Коротко: Рабочий прототип на Python по теме «llm video to txt».

## Что здесь

- Назначение: Рабочий прототип на Python по теме «llm video to txt».
- Основной стек: Python.
- Видимость: публичный репозиторий.
- Статус: активный репозиторий; актуальность проверять по issues и последним коммитам.

## Где смотреть работу

- Задачи и текущие решения: GitHub Issues этого репозитория.
- Код и материалы: файлы в корне и профильные папки проекта.
- Связь с HQ: если проект влияет на продукт, контент или воронку, сверяйте канон в `0_hq` и репозитории-владельце.

## Для агентов

- Сначала прочитайте этот README и открытые issues.
- Не переносите сюда канон соседних проектов без ссылки на источник.
- Перед правками проверьте существующие scripts, package.json/pyproject и локальные инструкции.

---

## Исходный README

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
