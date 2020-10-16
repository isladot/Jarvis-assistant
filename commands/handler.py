import json
import speech_recognition as sr
from services import speak as sp

with open('.\\.\\config.json', 'r') as config:
    data = json.load(config)
    config.close()
WAKE = data['wake']

def there_exists(terms, query):
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
        except Exception as e:
            print(str(e))
        return query.lower()

from commands.misc import name
from commands.utils import time, search
def respond(query):
    if 'what is your name' in query:
        name.name('Jarvis')
    if 'what time is it' in query:
        time.time('%H:%M')
    if 'search' in query:
        search.main(query)
    if there_exists(['exit', 'stop'], query):
        sp.watson_speak('Goodbye Sir.')
        exit()

def singleCommandHandler():
    print('Listening')
    query = record_audio()
    print(query)
    respond(query)


def bgCommandsHandler():
    while True:
        print('Listening')
        audio = record_audio()
        
        if audio.count(WAKE) > 0:
            sp.watson_speak('Hi Sir, how can i help you?')
            query = record_audio()
            print(query)
            respond(query)