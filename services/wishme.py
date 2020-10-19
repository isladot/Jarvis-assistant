from services import speak
import os
import time

def wishMe(config):
    TITLE = config['title']
    if config['wakeupMusic'] == 1:
        os.startfile('services\\sounds\\highway_to_hell.mp3')
    speak.watson_speak(f'Welcome home {TITLE}.')
    