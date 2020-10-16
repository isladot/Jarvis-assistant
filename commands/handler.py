import json
import time
import datetime
import webbrowser
import speech_recognition as sr
from services import speak as sp

with open('.\\.\\config.json', 'r') as config:
    data = json.load(config)
    config.close()
WAKE = data['wake']

def there_exists(terms):
    for term in terms:
        if term in query:
            return True

def record_audio(ask = False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            sp.speak(ask)
        audio = r.listen(source)
        query = ''
        try:
            query = r.recognize_google(audio)
        except sr.RequestError:
            sp.speak('Spiacente Signore, i miei sistemi non funzionano correttamente.')
        return query.lower()

def respond(query):
    if 'what is your name' in query:
        sp.speak('My name is Jarvis.')
    if 'what time is it' in query:
        strTime = datetime.datetime.now().strftime("%H:%M")
        sp.speak(f'It\'s {strTime}')
    if 'search' in query:
        search = record_audio('What do you want to search?')
        url = 'https://google.com/search?q=' + search
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open_new_tab(url)
        sp.speak('There are the results for ' + search)
    if there_exists(['exit', 'stop']):
        sp.watson_speak('Goodbye Sir.')
        exit()

while True:
    print('Listening')
    audio = record_audio()
    
    if audio.count(WAKE) > 0:
        sp.watson_speak('Hi Sir, how can i help you?')
        query = record_audio()
        print(query)
        respond(query)