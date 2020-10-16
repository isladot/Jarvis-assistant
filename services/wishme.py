import datetime
from services import speak

def wishMe(MASTER):
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak.google_speak("Buongiorno" + MASTER)
    elif hour>=12 and hour<18:
        speak.google_speak("Buonpomeriggio" + MASTER)
    else:
        speak.google_speak("Buonasera" + MASTER)

    speak.google_speak("Sono Jarvis. Come posso aiutarti?")
