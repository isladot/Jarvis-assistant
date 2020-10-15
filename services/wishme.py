import datetime
from services import speak

def wishMe(MASTER):
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak.speak("Buongiorno" + MASTER)
    elif hour>=12 and hour<18:
        speak.speak("Buonpomeriggio" + MASTER)
    else:
        speak.speak("Buonasera" + MASTER)

    speak.speak("Sono Jarvis. Come posso aiutarti?")