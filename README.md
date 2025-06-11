# 📝 Real-Time Voice Transcriber with LiveKit + AssemblyAI

This project is a real-time **speech-to-text transcriber** powered by:

- 🎙️ [LiveKit Agents](https://github.com/livekit/agents) — Manages audio room interactions
- 🧠 [AssemblyAI](https://www.assemblyai.com/) — Converts speech to text
- 🗂️ Python-based backend agent architecture

---

## 🚀 What It Does

- Connects to a LiveKit audio room
- Subscribes to audio tracks only
- Transcribes live speech using AssemblyAI
- Logs the transcription to console

---

## 🛠 Requirements

- Python 3.9+
- LiveKit Cloud account or self-hosted LiveKit server
- AssemblyAI API key

---

## 📦 Installation

1. Clone this repo
2. Install dependencies:
   ```bash
   pip install livekit-agents assemblyai python-dotenv
