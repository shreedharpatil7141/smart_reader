import speech_recognition as sr
from utils import log

def listen_raw(timeout=5, phrase_time_limit=5):
    """Listen and return raw recognized text."""
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            log("Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

        try:
            text = r.recognize_google(audio).lower()
            log(f"Heard: {text}")
            return text
        except Exception as e:
            log(f"[Voice Recognition Error] {e}")
            return ""
    except Exception as e:
        log(f"[Microphone Error] {e}")
        return ""


def wait_for_wake_word(wake_word="hey reader"):
    """Wait until user says the wake word."""

    log(f"Waiting for wake word: '{wake_word}'")
    while True:
        heard = listen_raw(timeout=5, phrase_time_limit=4)
        if wake_word in heard:
            log("Wake word detected!")
            return True


def listen_for_command():
    """After wake word is detected, listen for actual command."""
    log("Listening for command...")
    return listen_raw(timeout=5, phrase_time_limit=5)


def interpret_command(text):
    if not text:
        return None

    # Capture commands
    if any(cmd in text for cmd in ["capture", "start", "read", "take picture", "scan"]):
        return "capture"

    # Language commands
    if "english" in text:
        return ("lang", "en")
    if "hindi" in text:
        return ("lang", "hi")
    if "kannada" in text:
        return ("lang", "kn")
    if "tamil" in text:
        return ("lang", "ta")
    if "telugu" in text:
        return ("lang", "te")

    return None
