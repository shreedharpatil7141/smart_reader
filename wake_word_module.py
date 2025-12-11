import pvporcupine
import pyaudio
from utils import log

ACCESS_KEY = "nlc8OIzJ1pRTIMloTkuf7xWOUOrjkkFYgq/MX4ZXlrK8YEraoGxD/g=="
WAKE_WORD = "jarvis"   # Supported keyword


def create_porcupine_detector():
    porcupine = pvporcupine.create(
        access_key=ACCESS_KEY,
        keywords=[WAKE_WORD]
    )
    return porcupine


def listen_for_wake_word(callback):
    log("Wake-word listener started. Say 'Jarvis'...")

    porcupine = create_porcupine_detector()

    audio = pyaudio.PyAudio()
    stream = audio.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    try:
        while True:
            pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm_data = memoryview(pcm)

            result = porcupine.process(pcm_data)
            if result >= 0:
                log("Wake word detected: Jarvis")
                callback()
    except KeyboardInterrupt:
        pass
    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()
        porcupine.delete()
