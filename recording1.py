#new version of recording.py 
#might work??

from pvrecorder import PvRecorder
import wave, struct
from pydub import AudioSegment
import threading

def audio(stop_event):
    recorder = PvRecorder(device_index=0, frame_length=512)  # (32 milliseconds of 16 kHz audio)
    audio = []
    path = 'audio_recording.wav'
    try:
        recorder.start()

        while not stop_event.is_set():
            frame = recorder.read()
            audio.extend(frame)
    finally:
        recorder.stop()
        with wave.open(path, 'w') as f:
            f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
            f.writeframes(struct.pack("h" * len(audio), *audio))
        recorder.delete()
    return path
