import time
import webbrowser
import re
from services import speak as sp
from commands.handler import record_audio

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

async def googleSearch(kw):
    url = 'https://google.com/search?q=' + kw
    webbrowser.get(chrome_path).open_new_tab(url)
    response = 'These are the results on Google for ' + kw
    sp.speak(response)
    return response

async def youtubeSearch(kw):
    url = 'https://www.youtube.com/results?search_query=' + kw
    webbrowser.get(chrome_path).open_new_tab(url)
    response = 'These are the results on YouTube for ' + kw
    sp.speak(response)
    return response

async def stackoverflowSearch(kw):
    url = 'https://stackoverflow.com/search?q=' + kw
    webbrowser.get(chrome_path).open_new_tab(url)
    response = 'These are the results on Stackoverflow for ' + kw
    sp.speak(response)
    return response


SEARCH_PATTERN = {
    re.compile("search on google for [\w\s]+"): lambda kw: googleSearch(kw),
    re.compile("search on youtube for [\w\s]+"): lambda kw: youtubeSearch(kw),
    re.compile("search on stackoverflow for [\w\s]+") : lambda kw: stackoverflowSearch(kw)
}

async def main(query):
    for pattern, func in SEARCH_PATTERN.items():
        if pattern.match(query):
            kw = query.split('for ').pop()
            response = await func(kw)
            return response
            break