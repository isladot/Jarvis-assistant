#Internal Modules
import datetime
from main import speak

MASTER = "Luca"

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Buongiorno" + MASTER)
    elif hour>=12 and hour<18:
        speak("Buonpomeriggio" + MASTER)
    else:
        speak("Buonasera" + MASTER)
    
    speak("Sono Jarvis. Come posso aiutarti?")