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

r = sr.Recognizer()

def there_exists(terms):
    for term in terms:
        if term in query:
            return True

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            sp.speak(ask)
        audio = r.listen(source)
        query = ''
        try:
            query = r.recognize_google(audio, language='it-IT')
        except Exception as e:
            print('Errore: ' + str(e))
        except sr.RequestError:
            sp.speak('Spiacente Signore, i miei sistemi non funzionano correttamente.')
        return query.lower()

def respond(query):
    if 'come ti chiami' in query:
        sp.speak('Mi chiamo Jarvis')
    if 'che ore sono' in query:
        strTime = datetime.datetime.now().strftime("%H:%M")
        sp.speak(f'sono le {strTime}')
    if 'cerca' in query:
        search = record_audio('Per cosa vorresti effettuare la ricerca?')
        url = 'https://google.com/search?q=' + search
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open_new_tab(url)
        sp.speak('Ecco i risultati della ricerca per ' + search)
    if there_exists(['spegniti', 'chiuditi']):
        sp.watson_speak('Goodbye Sir.')
        exit()

while True:
    print('Listening')
    audio = record_audio()
    if audio.count(WAKE) > 0:
        sp.speak('Eccomi Sir, come posso aiutarla?')
        query = record_audio()
        respond(query)