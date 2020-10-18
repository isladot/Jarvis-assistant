import json
from tkinter import *
from PIL import ImageTk, Image

from services.wakeupJ import wakeupJarvis

with open('config.json', 'r') as data:
    config = json.load(data)
    data.close()

root = Tk()
root.title('J.A.R.V.I.S. Personal Assistant - powered by islaDevs')
root.iconphoto(False, PhotoImage(file='D:/GitHubRepositories/jarvis/gui/assets/images/JARVIS.png'))
root.geometry('700x500')
root.resizable(False, False)

#Header checkboxes section.
pcStartupV = IntVar()
programStartupV = IntVar()

headerSection = LabelFrame(root)
headerSection.pack(fill='x', side='top')

pcStartup = Checkbutton(headerSection, text='PC Startup Music', variable=pcStartupV)
pcStartup.grid(row=0, column=0)
programStartup = Checkbutton(headerSection, text='Wakeup Music', variable=programStartupV)
programStartup.grid(row=0, column=1)

#Body section
bodySection = LabelFrame(root)
bodySection.pack(fill='both', expand='yes')

#Bottom bottons section.
bottomSection = LabelFrame(root, pady=10)
bottomSection.pack(fill='x', side='bottom')
bottomSection.columnconfigure(0, weight=1)
bottomSection.columnconfigure(1, weight=1)

wakeButton = Button(bottomSection, text='Wake up Jarvis', command= lambda: wakeupJarvis(bodySection, config))
wakeButton.grid(row=0, column=0)
exitButton = Button(bottomSection, text='Shutdown Jarvis')
exitButton.grid(row=0, column=1)

#Main
root.mainloop()