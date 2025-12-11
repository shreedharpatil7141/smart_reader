import cv2
import pytesseract
from utils import log

def extract_text(image_path, lang="eng"):
    try:
        log(f"Preprocessing {image_path}")

        img = cv2.imread(image_path)
        if img is None:
            log("[ERROR] Could not load image.")
            return ""

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        proc = cv2.adaptiveThreshold(
            blur, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11, 2
        )

        log("Running Tesseract OCR")
        text = pytesseract.image_to_string(proc, lang=lang)

        log(f"OCR Result: {text}")
        return text.strip()

    except Exception as e:
        log(f"[OCR ERROR]: {e}")
        return ""
