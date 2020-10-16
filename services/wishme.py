from services import speak
import os
import time

def wishMe(TITLE):
    songs_dir = 'D:\\GitHubRepositories\\jarvis\\sounds'
    wish_song = os.listdir(songs_dir)[0]
    os.startfile(os.path.join(songs_dir, wish_song))
    speak.watson_speak(f'Welcome home {TITLE}.')
    