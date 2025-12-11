# utils.py
import requests
import time

def log(msg):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def check_internet(timeout=3):
    try:
        requests.get("https://www.google.com", timeout=timeout)
        return True
    except Exception:
        return False
