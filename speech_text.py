from google.cloud import speech 

client = speech.SpeechClient.from_service_account_file('key.json')

file_name = "test.mp3"

with open(file_name, 'rb') as i:
    mp3_data = i.read()

audio_file = speech.RecognitionAudio(content=mp3_data)

config = speech.RecognitionConfig(
    sample_rate_hertz=44100,
    enable_automatic_punctuation = True,
    language_code = "en-US"
)

response = client.recognize(
    config = config, 
    audio = audio_file
)

print(response)