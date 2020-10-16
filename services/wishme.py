from services import speak

def wishMe(TITLE):
    speak.watson_speak(f'Welcome home {TITLE}.')
