from tkinter import *
from services.wishme import wishMe

def wakeupJarvis(logSection, config):
    wakeupMessage = Label(logSection, text='Jarvis, waking up..', padx=6, pady=2)
    wakeupMessage.pack(anchor=W)
    wishMe(config)

