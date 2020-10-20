import os
import json
import random
import playsound

#.env configuration.
from dotenv import load_dotenv
load_dotenv(dotenv_path='.\\.\\.env')

API_KEY = os.getenv("IBM_WATSON_APIKEY")
API_URL = os.getenv("IBM_WATSON_URL")

#IBMWatson
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
text_to_speech = TextToSpeechV1(authenticator=IAMAuthenticator(API_KEY))
text_to_speech.set_service_url(API_URL)
def watson_speak(text):
    r = random.randint(1, 1000000)
    file_name = 'audio-' + str(r) + '.mp3'
    with open(file_name, 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                text,
                voice='en-US_HenryV3Voice',
                accept='audio/mp3'        
            ).get_result().content)
    playsound.playsound(file_name)
    os.remove(file_name)

#Pyttsx3
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

#GTTS
from gtts import gTTS
def google_speak(text):
    tts = gTTS(text=text, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

#WindowsSystem
import win32com.client as wincl
def windows_speak(text):
    tts = wincl.Dispatch("SAPI.SpVoice")
    tts.Speak(text)
