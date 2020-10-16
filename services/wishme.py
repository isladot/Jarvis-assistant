from services import speak

def wishMe(TITLE):
    speak.google_speak(f'Bentornato {TITLE}. C\'è qualcosa che posso fare per lei?')
