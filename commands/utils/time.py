from services import speak as sp
import datetime

def time(format):
    strTime = datetime.datetime.now().strftime(format)
    sp.speak(f'It\'s {strftime}')