# Video-Clipper
VideoClipper AI is a Python automation tool that converts long videos into ready-to-publish TikTok, YouTube Shorts, and Instagram Reels. It downloads or loads videos, transcribes speech with Whisper, selects the best clips, generates subtitles, creates vertical videos, and burns captions automatically using FFmpeg in a modular pipeline.

# 🎬 VideoClipper AI

VideoClipper AI is a Python-based automation pipeline that transforms long-form videos into ready-to-publish vertical short-form content for platforms such as TikTok, YouTube Shorts, and Instagram Reels.

The project automates the entire workflow from video input to final captioned vertical clips, significantly reducing the manual effort required for content repurposing.

## ✨ Features

* Download videos directly from YouTube using a URL
* Support local video files
* Automatic speech transcription using OpenAI Whisper
* Intelligent clip selection based on hook words, curiosity phrases, emotion detection, and scoring
* Automatic extraction of the best short clips
* Automatic SRT subtitle generation
* Vertical video generation (Crop and Blur styles)
* Burn professional subtitles directly into the video using FFmpeg
* Modular pipeline architecture
* Workspace-based processing system with automatic cleanup
* One-command execution through a single main script

## 📂 Project Workflow

```
Input Video
      │
      ▼
Transcription (Whisper)
      │
      ▼
Smart Clip Ranking
      │
      ▼
Clip Extraction
      │
      ▼
Subtitle Generation
      │
      ▼
Vertical Conversion
      │
      ▼
Subtitle Burning
      │
      ▼
Ready-to-Upload Shorts
```

## 🛠 Technologies Used

* Python 3
* OpenAI Whisper
* FFmpeg
* yt-dlp
* JSON
* subprocess
* os / shutil

## 📁 Project Structure

```
modules/
workspace/
config/
archive/
logs/

main.py
download_youtube.py
transcribe.py
```

The workspace system isolates temporary files from generated outputs, keeping the project organized and ensuring every run starts from a clean environment.

## 🚀 Future Improvements

* AI-powered clip ranking using LLMs
* Multi-niche support (Business, History, Education, Podcasts, etc.)
* Automatic title generation
* Automatic description generation
* Automatic hashtag generation
* Multi-language subtitle generation
* Speaker tracking for dynamic vertical cropping
* Automatic upload to social media platforms

## 🎯 Goal

The goal of this project is to automate the conversion of long-form videos into engaging, high-quality short-form content with minimal human intervention, making content creation faster and more scalable.

---

**Current Version:** VideoClipper AI V1 Stable

```
```
