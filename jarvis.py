import json
import asyncio
from tkinter import *
from PIL import ImageTk, Image

from commands.gui.asktoJarvis import asktoJarvis
from gui.wakeupJarvis import wakeupJarvis
from gui.shutdownJarvis import shutdownJarvis
from gui.configMusics import updateStartUpValue, updateWakeUpValue

with open('config.json', 'r') as data:
    config = json.load(data)
    data.close()

root = Tk()
root.title('J.A.R.V.I.S. Personal Assistant - powered by islaDevs')
root.iconphoto(False, PhotoImage(file='assets/images/JARVIS.png'))
root.geometry('700x500')
root.resizable(False, False)

#Header section declaration.
headerSection = LabelFrame(root)
headerSection.pack(fill='x', side='top')
headerSection.columnconfigure(0, weight=1)
headerSection.columnconfigure(1, weight=1)
headerSection.columnconfigure(2, weight=1)
#Log section declaration.
logSection = LabelFrame(root)
logSection.pack(fill='both', expand='yes')
#Bottom section declaration.
bottomSection = LabelFrame(root, pady=10)
bottomSection.pack(fill='x', side='bottom')
bottomSection.columnconfigure(0, weight=1)
bottomSection.columnconfigure(1, weight=1)
bottomSection.columnconfigure(2, weight=1)

##Header section configuration.
#Checkbox + related variable for startupMusic config parameter.
pcStartupV = IntVar(headerSection, config['startupMusic'])
pcStartup = Checkbutton(headerSection, text='PC Startup Music', anchor=W, variable=pcStartupV, command= lambda: updateStartUpValue(pcStartupV, config))
pcStartup.grid(row=0, column=0, sticky=W+E)
#Checkbox + related variable for wakeupMusic config parameter.
programStartupV = IntVar(headerSection, config['wakeupMusic'])
programStartup = Checkbutton(headerSection, text='Wakeup Music', anchor=W, variable=programStartupV, command= lambda: updateWakeUpValue(programStartupV, config))
programStartup.grid(row=0, column=1, sticky=W+E)
#Button to clear log section.
def clearLogs():
    for widget in logSection.winfo_children():
        widget.destroy()
clearlogButton = Button(headerSection, text='Clear Logs', command= clearLogs)
clearlogButton.grid(row=0, column=2, sticky=W+E)

##Log section configuration.

##Bottom section configuration.
#Button to Wake up Jarvis.
wakeButton = Button(bottomSection, text='Wake up Jarvis',  command= lambda: wakeupJarvis(logSection, config))
wakeButton.grid(row=0, column=0, sticky=W+E, padx=20)
#Button to Ask to Jarvis something.
askButton = Button(bottomSection, text='Ask to Jarvis', command= lambda: asyncio.run(asktoJarvis(logSection, config)))
askButton.grid(row=0, column=1, sticky=W+E, padx=20)
#Button to Kill Jarvis.
exitButton = Button(bottomSection, text='Shutdown Jarvis', command= lambda: shutdownJarvis(logSection, config))
exitButton.grid(row=0, column=2, sticky=W+E, padx=20)

#Main
root.mainloop()