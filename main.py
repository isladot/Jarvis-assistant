import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

print("Jarvis, avvio in corso..")

master = "Luca"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Buongiorno" + master)

    elif hour>=12 and hour<18:
        speak("Buonpomeriggio" + master)

    else:
        speak("Buonasera" + master)
    
    speak("Sono Jarvis. Come posso aiutarti?")

wishMe()
