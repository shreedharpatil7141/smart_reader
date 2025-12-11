from gtts import gTTS
import pyttsx3
import os
from utils import log

# ---------------- ONLINE SPEECH ----------------
def speak_online(text, lang="en"):
    try:
        log(f"Online speech: {text}")
        tts = gTTS(text=text, lang=lang)
        tts.save("online.mp3")
        os.system("mpg123 online.mp3 > /dev/null 2>&1")
    except Exception as e:
        log(f"[ERROR] Online TTS failed: {e}")

# ---------------- OFFLINE SPEECH ----------------
def speak_offline(text, lang="en"):
    try:
        log(f"Offline speech: {text}")
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        log(f"[ERROR] Offline TTS failed: {e}")

# -------------- Universal Speak Wrapper ---------------
def speak(text, lang="en", online=False):
    if online:
        speak_online(text, lang)
    else:
        speak_offline(text, lang)

