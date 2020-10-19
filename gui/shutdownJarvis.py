from services import speak

def shutdownJarvis(logSection, config):
    TITLE = config['title']
    speak.watson_speak(f'Goodbye {TITLE}.')
    exit()