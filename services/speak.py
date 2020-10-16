import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def google_speak(text):
    engine.say(text)
    engine.runAndWait()

import playsound
import os
import random
from gtts import gTTS

def google_speak(text):
    tts = gTTS(text=text, lang='it')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)