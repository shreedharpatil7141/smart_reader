from deep_translator import GoogleTranslator
from utils import log
import requests

def translate_text(text, src_lang="en", dst_lang="en", offline=False):
    """
    Hybrid translation:
    - If offline=True ? always return English text
    - If offline=False ? try online translation
    - If online fails ? fallback to English text
    """
    
    # OFFLINE MODE ? English ONLY
    if offline:
        log("Offline mode: Skipping translation. Returning English only.")
        return text

    # ONLINE MODE ? Attempt translation
    try:
        log(f"Online translation: {src_lang} ? {dst_lang}")
        result = GoogleTranslator(source=src_lang, target=dst_lang).translate(text)
        return result

    except Exception as e:
        log(f"Translation failed, fallback to English only: {e}")
        return text

