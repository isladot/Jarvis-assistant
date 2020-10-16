#External Modules
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
#Internal Modules
import os
import json
import time
import datetime
import webbrowser

from services import speak as sp, wishme as wm

with open('config.json', 'r') as config:
    data = json.load(config)
    config.close()

WAKE = data['wake']
TITLE = data['title']
MASTER = data['master']

print("Jarvis, avvio in corso..")
wm.wishMe(TITLE)

from commands import handler
