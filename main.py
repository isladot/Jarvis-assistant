#External Modules
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
#Internal Modules
import datetime
import webbrowser
import os
import json

from services import speak as sp, wishme as wm

with open('config.json', 'r') as config:
    data = json.load(config)
    config.close()

MASTER = data['master']

sp.speak("Jarvis, avvio in corso..")
wm.wishMe(MASTER)

from commands import handler as hlr
##
"""
if 'aggiorna' and 'master' in query:
    data['master'] = 'Giovanni'
    with open('config.json', 'w') as config:
        json.dump(data, config)
        config.close()

elif 'apri youtube' in query:
    url = 'youtube.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open_new_tab(url)

elif 'che ore sono' in query:
    strTime = datetime.datetime.now().strftime("%H:%M")
    sp.speak(f'sono le {strTime}')
"""