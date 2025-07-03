import os
import pyttsx3
import speech_recognition as sr
import requests

# Initialize voice engine (macOS)
engine = pyttsx3.init(driverName='nsss')

# Set FLAC encoder path for Apple Silicon
sr.AudioFile.FLAC_converter = "/opt/homebrew/bin/flac"

# Initialize conversation memory
conversation_history = []

# 🎙 Text-to-speech
def speak(text):
    print(f"\n🤖: {text}\n")
    engine.say(text)
    engine.runAndWait()

# 🎧 Speech-to-text
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening... Speak now.")
        audio = recognizer.listen(source)
    try:
        print("🧠 Transcribing...")
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I could not understand what you said."
    except sr.RequestError as e:
        return f"Speech recognition failed: {e}"

# 🧠 Ask llama3 via Ollama
def query_llama3(prompt):
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    })
    return response.json()['response']

# 💬 Get interviewer-style feedback
def get_feedback(user_input):
    conversation_history.append(f"Candidate: {user_input}")
    
    full_prompt = f"""{system_prompt}

Conversation so far:
{chr(10).join(conversation_history)}

Your turn as the interviewer:"""

    response = query_llama3(full_prompt)
    conversation_history.append(f"Interviewer: {response}")
    return response

# 🧠 Tech Lead Interviewer Prompt
system_prompt = """
You are a senior backend engineer conducting a real system design interview.

- Ask realistic and tough system design questions (e.g., API Gateway, Rate Limiter, Message Queue)
- If the candidate gives an incorrect answer, say clearly:
    - "You are wrong because..."
    - "Instead, you should say..." and explain the correct reasoning
- If the answer is good, highlight strengths and follow up with deeper challenges
- Ask only one follow-up at a time
- Act like a serious but fair interviewer, not a tutor
- Keep the tone professional, and push for deeper tradeoffs (availability, consistency, latency, etc.)
"""

# 🚀 Main loop
def main():
    print("🤖 System Design Interviewer (LLaMA 3 via Ollama) is ready.")
    speak("Welcome! Let's begin your system design interview. Design a URL shortening service.")

    while True:
        user_input = listen()

        if user_input.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye! Great job today.")
            break

        feedback = get_feedback(user_input)
        speak(feedback)

if __name__ == "__main__":
    main()