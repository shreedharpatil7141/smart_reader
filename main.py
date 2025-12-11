import time
from gpiozero import Button
from camera_module import capture_image
from ocr_module import extract_text
from speech_module import speak_online, speak_offline
from translation_module import translate_text
from utils import log

# -------------------------------
# GPIO PIN ASSIGNMENTS
# -------------------------------
BTN_CAMERA = 17      # Camera capture
BTN_EN = 27         # English
BTN_KN = 22         # Kannada
BTN_HI = 23         # Hindi
BTN_TE = 24         # Telugu

# -------------------------------
# BUTTON SETUP
# -------------------------------
btn_camera = Button(BTN_CAMERA, pull_up=True)
btn_en = Button(BTN_EN, pull_up=True)
btn_kn = Button(BTN_KN, pull_up=True)
btn_hi = Button(BTN_HI, pull_up=True)
btn_te = Button(BTN_TE, pull_up=True)

current_text = ""     # OCR result stored
ocr_ready = False      # Changes to True after capture


# -------------------------------
# LANGUAGE TRANSLATION HANDLER
# -------------------------------
def handle_language(lang_code, lang_name):
    global current_text, ocr_ready

    if not ocr_ready or not current_text:
        speak_online("Please capture text first.", "en")
        return

    log(f"Translating to {lang_name}")
    speak_online(f"Translating to {lang_name}", "en")

    translated = translate_text(current_text, "en", lang_code, offline=False)

    if not translated:
        speak_online("Translation failed.", "en")
        return

    speak_online(translated, lang_code)

    # Reset state
    ocr_ready = False
    current_text = ""
    speak_online("Ready for next capture.", "en")


# -------------------------------
# CAMERA CAPTURE HANDLER
# -------------------------------
def handle_camera_press():
    global current_text, ocr_ready

    log("Camera button pressed once. Waiting for second press.")
    speak_online("Camera button. Press again to capture.", "en")

    start = time.time()
    while time.time() - start < 3:  # 3-second window for double press
        if not btn_camera.is_pressed:
            continue
        time.sleep(0.2)

        log("Capturing image...")
        speak_online("Capturing image.", "en")

        img_path = capture_image()
        text = extract_text(img_path)

        if not text:
            speak_online("Could not read text. Try again.", "en")
            return

        current_text = text
        ocr_ready = True

        speak_online("Text captured. Press a language button to translate.", "en")
        return


# -------------------------------
# MAIN LOOP
# -------------------------------
def main():
    speak_online("System ready. Use buttons to operate.", "en")
    log("System ready.")

    while True:
        if btn_camera.is_pressed:
            handle_camera_press()

        if btn_en.is_pressed:
            handle_language("en", "English")

        if btn_kn.is_pressed:
            handle_language("kn", "Kannada")

        if btn_hi.is_pressed:
            handle_language("hi", "Hindi")

        if btn_te.is_pressed:
            handle_language("te", "Telugu")

        time.sleep(0.1)


if __name__ == "__main__":
    main()
