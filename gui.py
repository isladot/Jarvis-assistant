import json
from tkinter import *
from PIL import ImageTk, Image

from services.wakeupJarvis import wakeupJarvis
from commands.asktoJarvis import asktoJarvis
from services.shutdownJarvis import shutdownJarvis
from services.configMusics import updateStartUpValue, updateWakeUpValue

with open('config.json', 'r') as data:
    config = json.load(data)
    data.close()

root = Tk()
root.title('J.A.R.V.I.S. Personal Assistant - powered by islaDevs')
root.iconphoto(False, PhotoImage(file='D:/GitHubRepositories/jarvis/gui/assets/images/JARVIS.png'))
root.geometry('700x500')
root.resizable(False, False)

#Header checkboxes section.
headerSection = LabelFrame(root)
headerSection.pack(fill='x', side='top')

pcStartupV = IntVar(headerSection, config['startupMusic'])
programStartupV = IntVar(headerSection, config['wakeupMusic'])

pcStartup = Checkbutton(headerSection, text='PC Startup Music', variable=pcStartupV, command= lambda: updateStartUpValue(pcStartupV, config))
pcStartup.grid(row=0, column=0)
programStartup = Checkbutton(headerSection, text='Wakeup Music', variable=programStartupV, command= lambda: updateWakeUpValue(programStartupV, config))
programStartup.grid(row=0, column=1)

#Body section
logSection = LabelFrame(root)
logSection.pack(fill='both', expand='yes')

#Bottom bottons section.
bottomSection = LabelFrame(root, pady=10)
bottomSection.pack(fill='x', side='bottom')
bottomSection.columnconfigure(0, weight=1)
bottomSection.columnconfigure(1, weight=1)
bottomSection.columnconfigure(2, weight=1)


wakeButton = Button(bottomSection, text='Wake up Jarvis', padx=20,  command= lambda: wakeupJarvis(logSection, config))
wakeButton.grid(row=0, column=0)
askButton = Button(bottomSection, text='Ask to Jarvis', padx=20, command= lambda: asktoJarvis(logSection, config))
askButton.grid(row=0, column=1)
exitButton = Button(bottomSection, text='Shutdown Jarvis', padx=20, command= lambda: shutdownJarvis(logSection, config))
exitButton.grid(row=0, column=2)

#Main
root.mainloop()