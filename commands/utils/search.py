from services import speak as sp
from commands.handler import record_audio
import webbrowser

def search(site):
    if site == 'google':
        query = record_audio('What do you want to search on Google?')
        url = 'https://google.com/search?q=' + query
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open_new_tab(url)
        sp.speak('These are the results for ' + query)
    elif site == 'youtube':
        query = record_audio('What do you want to search on YouTube?')
        url = 'https://www.youtube.com/results?search_query=' + query
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open_new_tab(url)
        sp.speak('These are the results for ' + query)
