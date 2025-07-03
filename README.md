# 🧠 Voice-Based System Design Interviewer (Offline, Local LLM)

This project is an AI-powered **voice-interactive system design interviewer** that behaves like a **Tech Lead** at top tech companies. It challenges your answers, gives direct feedback, and asks realistic follow-up questions — all offline using **Meta’s LLaMA 3 model via Ollama**.

---

## 🎯 Features

- 🎤 Voice input/output (via your mic & speakers)
- 🧠 LLaMA 3 (8B) via Ollama (runs locally, no internet)
- 💬 Tech Lead-style feedback with tough follow-up questions
- ❌ Clearly tells you when you're wrong and shows correct alternatives
- 🔁 Maintains conversation context
- 🧪 Practice system design interviews anytime, privately

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Ramana-Vanchanagiri/system-design-interviewer.git
cd system-design-interviewer ```

### 2. Create and activate virtual environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
brew install flac  # for macOS users (required by SpeechRecognition)
🤖 Ollama (LLaMA 3 Local Model)
1. Install Ollama
bash
Copy
Edit
brew install ollama
Or download it from https://ollama.com/download

2. Run the model
bash
Copy
Edit
ollama run llama3
Leave this terminal open — it will host your LLM at http://localhost:11434.

🧑‍💻 Run the App
bash
Copy
Edit
python app.py
🎤 Speak your answers aloud.

🧠 Get technical feedback and follow-up questions.

❌ Say “exit” or press Ctrl + C to quit.

📂 Project Structure
perl
Copy
Edit
system-design-interviewer/
├── app.py              # Main application logic
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md           # You're here
📌 Tech Stack
Python 3

pyttsx3 (Text-to-speech)

SpeechRecognition (Voice input)

FLAC (required for audio encoding)

Ollama + LLaMA 3 (Offline LLM)

📚 Possible Enhancements
Save transcripts and feedback to file

Random question bank loader

Use Whisper for full offline voice transcription

Add typing (text) mode fallback

Add difficulty levels or scenario-based drills

🙏 Acknowledgements
Meta's LLaMA 3

Ollama for free, local LLMs

Python OSS community ❤️

Made with 💻 and 🧠 to help engineers practice system design — privately, locally, and smartly.

yaml
Copy
Edit

---

Let me know if you want a matching `requirements.txt` and `.gitignore` too. Ready when you are!








Ask ChatGPT
