import subprocess
import uuid
from utils import log

def capture_image():
    """Capture an image using rpicam-still on Raspberry Pi."""

    try:
        filename = f"img_{uuid.uuid4().hex}.jpg"

        cmd = [
            "rpicam-still",
            "-o", filename,
            "--nopreview",
            "--immediate",
            "--encoding", "jpg",
            "-t", "1"
        ]

        log(f"Running: {' '.join(cmd)}")
        proc = subprocess.run(cmd, capture_output=True, text=True)

        if proc.returncode != 0:
            log(f"[ERROR] Camera error: {proc.stderr}")
            return None

        log(f"Image saved as: {filename}")
        return filename

    except Exception as e:
        log(f"[ERROR] Camera capture failed: {e}")
        return None
