import os
import directions
from google.cloud import texttospeech


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'
client = texttospeech.TextToSpeechClient()

# text is where the google maps direction will go
raw_text = "Walk 2 minutes to the Austin History Center Station. Board the bus. Get off at the UT West Mall Station."

synthesis_input = texttospeech.SynthesisInput(text=raw_text)

voice = texttospeech.VoiceSelectionParams(
    language_code = "en-US",
    name = "en-US-Studio-O"
)

audio_config = texttospeech.AudioConfig(
    audio_encoding = texttospeech.AudioEncoding.MP3,
    effects_profile_id = ["small-bluetooth-speaker-class-device"],
    speaking_rate = 1,
    pitch = 1
)

response = client.synthesize_speech(
    input = synthesis_input,
    voice = voice,
    audio_config = audio_config
)

with open("speech.mp3", "wb") as i:
    i.write(response.audio_content)
