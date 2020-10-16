from services import speak as sp
from commands.handler import record_audio
import webbrowser
import re

def googleSearch(kw):
    url = 'https://google.com/search?q=' + kw
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open_new_tab(url)
    sp.speak('These are the results for ' + kw)

def youtubeSearch(kw):
    url = 'https://www.youtube.com/results?search_query=' + kw
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open_new_tab(url)
    sp.speak('These are the results for ' + kw)

SEARCH_PATTERN = {
    re.compile("search on google for [\w\s]+"): lambda kw: googleSearch(kw),
    re.compile("search on youtube for [\w\s]+"): lambda kw: youtubeSearch(kw)
}

def main(query):
    for pattern, func in SEARCH_PATTERN.items():
        if pattern.match(query):
            kw = query.split('for ').pop()
            func(kw)
            break