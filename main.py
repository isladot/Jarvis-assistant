#External Modules
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
#Internal Modules
import datetime
import webbrowser
import os
import smtplib
import json

with open("config.json", "r") as config:
    data = json.load(config)
    config.close()

MASTER = data['master']

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Buongiorno" + MASTER)
    elif hour>=12 and hour<18:
        speak("Buonpomeriggio" + MASTER)
    else:
        speak("Buonasera" + MASTER)
    
    speak("Sono Jarvis. Come posso aiutarti?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("In ascolto..")
        audio = r.listen(source)
    
    try:
        print("Riconoscimento..")
        query = r.recognize_google(audio, language='it-IT')
        print(f"Il padrone ha detto: {query}\n")

    except Exception as e:
        print("Ripetere, grazie.")

print("Jarvis, avvio in corso..")
wishMe()
#takeCommand()