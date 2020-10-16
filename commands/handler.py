import time
import datetime
import webbrowser
import speech_recognition as sr
from services import speak as sp

r = sr.Recognizer()

def there_exists(terms):
    for term in terms:
        if term in query:
            return True

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            sp.google_speak(ask)
        audio = r.listen(source)
        query = ''
        try:
            query = r.recognize_google(audio, language='it-IT')
        except sr.UnknownValueError:
            sp.google_speak('Spiacente padrone, non ho capito bene.')
        except sr.RequestError:
            sp.google_speak('Spiacente padrone, il mio sistema non funziona correttamente.')
        return query.lower()

def respond(query):
    if 'come ti chiami' in query:
        sp.google_speak('Mi chiamo Jarvis')
    if 'che ore sono' in query:
        strTime = datetime.datetime.now().strftime("%H:%M")
        sp.google_speak(f'sono le {strTime}')
    if 'cerca' in query:
        search = record_audio('Per cosa vorresti effettuare la ricerca?')
        url = 'https://google.com/search?q=' + search
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open_new_tab(url)
    if there_exists(['stop', 'exit', 'chiudi']):
        sp.google_speak('Arrivederci padrone.')
        exit()

time.sleep(1)
sp.google_speak('Come posso aiutarti?')
while 1:
    query = record_audio()
    respond(query)