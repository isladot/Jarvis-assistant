import asyncio
from tkinter import *
import speech_recognition as sr

from services import speak as sp
from commands import handler as hdl

async def asktoJarvis(logSection, config):
    listeningMessage = Label(logSection, text='Listening for instructions..', padx=6, pady=2)
    listeningMessage.pack(anchor=W)
    listeningMessage.after(10, lambda: asyncio.run(commandOutputs(logSection)))

async def commandOutputs(logSection):
    query = hdl.record_audio()
    response = await hdl.respond(query)
    logMessage = Label(logSection, text=response, padx=6, pady=2)
    logMessage.pack(anchor=W)