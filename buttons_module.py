from utils import log

def wait_for_language_press():
    log("Press ENTER to choose the language...")
    input()
    return True

def wait_for_capture():
    log("Press ENTER to capture image...")
    input()
    return True
