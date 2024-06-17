from google.cloud import speech 

#establishes client connection
client = speech.SpeechClient.from_service_account_file('key.json')

#sets file name
file_name = "test.mp3"

#reads in the mp3 data
with open(file_name, 'rb') as i:
    mp3_data = i.read()

#sets audio file and instantiates the recongition process
audio_file = speech.RecognitionAudio(content=mp3_data)

#sets speed and language for the voice
config = speech.RecognitionConfig(
    sample_rate_hertz=44100,
    enable_automatic_punctuation = True,
    language_code = "en-US"
)

#finishes client session
response = client.recognize(
    config = config, 
    audio = audio_file
)

print(response)
