#import required modules
import time as t
import keyboard
from tkinter import *
import tkinter
import os
from pathlib import Path
import random as r
from playsound import playsound
import json

test = 'hello git'
gui = Tk()
Fvar = StringVar()
Ovar = StringVar()
Dvar = StringVar()
Svar = StringVar()
ORvar = StringVar()
Fvar.set("SELECT FOLDER")

def stemFile(file):
    stemmed = Path(file).stem
    return(stemmed)

Ovar.set("Operator")
Dvar.set("Destination")
Svar.set("Station")
ORvar.set("Origin")
Folders = os.listdir("Sounds")
Stations = ["Station"]
Destinations = ["Destination"]
Operators = ["Operator"]

def OnFupdate(event):
    print(event)
    ORvar.set('')
    Dvar.set('')
    DestinationEntry['menu'].delete(0,'end')
    OriginEntry['menu'].delete(0,'end')
    OperatorEntry['menu'].delete(0,'end')
    Stations = os.listdir(os.path.join("Sounds", Fvar.get(), "stations"))
    Destinations = os.listdir(os.path.join("Sounds", Fvar.get(), "dest"))
    Operators = os.listdir(os.path.join("Sounds", Fvar.get(), "operators"))
    defaultsPath = os.path.join("Sounds", Fvar.get(), "defaults.txt")
    defaultsFile = open(defaultsPath)
    defaults = json.load(defaultsFile)
    ORvar.set(defaults["Origin"])
    Dvar.set(defaults["Destination"])
    Svar.set(defaults["Station"])
    Ovar.set(defaults["Operator"])
    
    Stations = map(stemFile, Stations)
    Destinations = map(stemFile, Destinations)
    Operators = map(stemFile, Operators)
    for choice in Destinations:
        DestinationEntry['menu'].add_command(label=choice, command=tkinter._setit(Dvar, choice))
    for choice in Operators:
        OperatorEntry['menu'].add_command(label=choice, command=tkinter._setit(Ovar, choice))
    for choice in Stations:
        OriginEntry["menu"].add_command(label=choice, command=tkinter._setit(ORvar, choice))

icon = PhotoImage(file="UI\\BRlogo.png")
gui.iconphoto(False, icon)
gui.title("BR Announcer")

#Set Variables5t
def Run():
    Extras = os.listdir(os.path.join("Sounds", Fvar.get(), "extra"))
    Epath = os.path.join("Sounds", Fvar.get(), "extra")
    Stations = os.listdir(os.path.join("Sounds", Fvar.get(), "stations"))
    Destinations = os.listdir(os.path.join("Sounds", Fvar.get(), "dest"))
    Operators = os.listdir(os.path.join("Sounds", Fvar.get(), "operators"))
    Stations = map(stemFile, Stations)
    Destinations = map(stemFile, Destinations)
    Operators = map(stemFile, Operators)
    FolderLabel.config(text="Loading...")
    doorCounter = 0
    StopList = []
    LastStopList = []
    defaultsPath = os.path.join("Sounds", Fvar.get(), "defaults.txt")
    defaultsFile = open(defaultsPath)
    defaults = json.load(defaultsFile)
    keybind = defaults["Keybinds"]
    MainStation = defaults["MainStations"]
    
    StartupButton.destroy()
    FolderLabel.destroy()
    
    
    icon = PhotoImage(file="UI\\BRlogo.png", master=gui)
    gui.iconphoto(False, icon)
    gui.title("BR Announcer - Route Maker")
    def UpdateUI():
        print(StopList)
        print("Updating UI")
        ListBox.delete(0,END)
        for x in StopList:
            ListBox.insert(END, x)
        ListBox.see(ListBox.size())
    def AddStation():
        station = Svar.get()
        StopList.append(station)
        UpdateUI()
    def RemoveStation():
        times = 0
        for x in ListBox.curselection():
            StopList.pop(x-times)
            times = times + 1     
        UpdateUI()
    def Done():
        gui.destroy()
    def LegaliseFile(fn):
        illegalChars = '<>:"/|?*\\.'
        for char in fn:
            if char in illegalChars:
                fn = fn.replace(char,'')
        if fn == "":
            print("Defaulting to automatic...")
            fn = (Fvar.get()+Ovar.get()+ORvar.get()+Dvar.get())
            return(fn)
        print(fn)
        return(fn)

    def Save():
        filename = laveEntry.get()
        filename = LegaliseFile(filename)
        filePath = os.path.join("SaveData",(filename + ".txt"))
        SaveDict = {"Folder":Fvar.get(),"Origin":ORvar.get(),"Destination":Dvar.get(),"Stations":StopList,"Operator":Ovar.get()}
        f = open(filePath,"w")
        json.dump(SaveDict,f)
        laveLabel.config(text="Saved",fg="Green")
    def Load():
        loadName = laveEntry.get()
        loadName = LegaliseFile(loadName)
        filePath = os.path.join("SaveData",(loadName + ".txt"))
        if os.path.exists(filePath):
            f = open(filePath)
            data = json.load(f)
            Fvar.set(data["Folder"])
            ORvar.set(data["Origin"])
            Dvar.set(data["Destination"])
            Ovar.set(data["Operator"])
            print(ORvar.get())
            StopList.clear()
            for x in data["Stations"]:
                StopList.append(x)
            UpdateUI()
        else:
            laveLabel.config(text="NOT FOUND",fg="Red")
            


    StationLabel = Label(gui, text="Enter Station:")
    ListLabel = Label(gui, text="Stops Added:")
    ListBox = Listbox(gui,selectmode=MULTIPLE)
    ListScroll = Scrollbar(gui)
    ListBox.config(yscrollcommand=ListScroll.set)
    ListScroll.config(command=ListBox.yview)
    Stations = os.listdir(os.path.join("Sounds", Fvar.get(), "stations"))
    Stations = map(stemFile, Stations)
    StationEntry = OptionMenu(gui, Svar, *Stations)
    StationEntry.config(width=15)
    AddButton = Button(gui, text="Add Station", command=AddStation)
    DelButton = Button(gui, text="Remove", command=RemoveStation)
    DoneButton = Button(gui, text="Done", command=Done)
    SaveButton = Button(gui, text="Save", command=Save)
    LoadButton = Button(gui, text="Load", command=Load)
    laveLabel = Label(gui, text="Save/Load Name:")
    laveEntry = Entry(gui)
    DoneButton.grid(row=9,column=0,sticky=W,pady=2)
    StationLabel.grid(row=1,column=0,sticky=W,pady=2)
    StationEntry.grid(row=1, column=1,sticky=W,pady=2)
    ListLabel.grid(row=3, column=0,sticky=W,pady=2)
    ListBox.grid(row=4, column=0, sticky=W,pady=2)
    ListScroll.grid(row=4, column=1, sticky=W, pady=2)
    DelButton.grid(row=2,column=1,sticky=W,pady=2)
    AddButton.grid(row=2,column=0,sticky=W,pady=2)
    OriginEntry.grid(row = 0,column = 1, sticky= W, pady=2,padx=10)
    DestinationEntry.grid(row = 5,column=1,sticky=W,pady=2, padx=10)
    OperatorEntry.grid(row=6,column=1,sticky=W,pady=2,padx=10)
    OriginLabel.grid(row=0,column=0,sticky=W,pady=2)
    DestinationLabel.grid(row=5,column=0,sticky=W,pady=2)
    OperatorLabel.grid(row=6, column=0,sticky=W,pady=2)
    SaveButton.grid(row=7,column=0,sticky=W,pady=2)
    LoadButton.grid(row=7,column=1,sticky=W,pady=2)
    laveLabel.grid(row=8,column=0,sticky=W,pady=2)
    laveEntry.grid(row=8,column=1,sticky=W,pady=2)
    gui.mainloop()
    
    def Announce(stop):
        stopRoot = stop
        stop = stop + ".mp3"
        sAudio = os.path.join(sPath, stop)#AS.from_mp3(os.path.join(sPath, stop))
        playsound(sAudio)
        
        if Calling == True and StopList.index(stopRoot) == len(StopList) - 1:
            playsound(And)
            playsound(destination)
        return
    
    Folder = os.path.join("Sounds", Fvar.get())
    Welcome = os.path.join(Folder, "info", "Welcome.mp3")#AS.from_mp3(os.path.join(Folder, "info", "Welcome.mp3"))
    ServiceTo = os.path.join(Folder, "info", "ServiceTo.mp3")#AS.from_mp3(Folder +"\\info" + "\\ServiceTo.mp3")
    NextStation = os.path.join(Folder, "info", "NextStation.mp3")#AS.from_mp3(Folder +"\\info" + "\\NextStation.mp3")
    Terminate = os.path.join(Folder, "info", "Terminate.mp3")#AS.from_mp3(Folder +"\\info" + "\\Terminate.mp3")
    Only = os.path.join(Folder, "info", "Only.mp3")#AS.from_mp3(Folder +"\\info" + "\\Only.mp3")
    CallingAt = os.path.join(Folder, "info", "CallingAt.mp3")#AS.from_mp3(Folder +"\\info" + "\\CallingAt.mp3")
    And = os.path.join(Folder, "info", "And.mp3")#AS.from_mp3(Folder +"\\info" + "\\And.mp3")
    ThisIs = os.path.join(Folder, "info", "ThisIs.mp3")#AS.from_mp3(os.path.join(Folder, "info", "ThisIs.mp3"))
    operator = Ovar.get() + ".mp3"
    origin = ORvar.get()
    destination = Dvar.get()

    if StopList:
        if StopList[0] == origin:
            StopList.pop(0)
    if StopList:
        if StopList[-1] == destination:
            StopList.pop()
    destination=Dvar.get() + ".mp3"
    sPath = os.path.join(Folder, 'stations')
    oPath = os.path.join(Folder, 'operators')
    dPath = os.path.join(Folder, 'dest')
    operator = os.path.join(oPath, operator)
    destination = os.path.join(dPath, destination)
    

    LastStopList.append(origin)
    print(StopList)
    Calling = False
    #This Does announcements
    while len(StopList) > 0:
        if keyboard.is_pressed(keybind[0]) or keyboard.is_pressed(keybind[1]):
            Announcer = True
            doorCounter = doorCounter + 1
        if doorCounter == 1 and Announcer == True:
            t.sleep(5)
            playsound(ThisIs)
            Announce(LastStopList[0])
            playsound(NextStation)
            Announce(StopList[0])
            Announcer = False
        if doorCounter == 2:
            t.sleep(25)
            playsound(Welcome)
            playsound(operator)
            playsound(ServiceTo)
            playsound(destination)
            if LastStopList[0] in MainStation:
                Calling = True
                playsound(CallingAt)
                for x in StopList:
                    Announce(x)
                Calling = False
            playsound(NextStation)
            Announce(StopList[0])
            LastStopList.pop(0)
            LastStopList.append(StopList[0])
            StopList.pop(0)
            doorCounter = 0          
        if keyboard.is_pressed(keybind[2]):
            if Extras:
                sRandom = os.path.join(Epath, r.choice(Extras))
                playsound(sRandom)
    LastStop = True
    while LastStop == True:
        if keyboard.is_pressed(keybind[0]) or keyboard.is_pressed(keybind[1]):
            Announcer = True
            doorCounter = doorCounter + 1
        if keyboard.is_pressed(keybind[2]):
            if Extras:
                sRandom = os.path.join(Epath, r.choice(Extras))
                playsound(sRandom)
        if doorCounter == 1 and Announcer == True:
            t.sleep(5)
            playsound(ThisIs)
            Announce(LastStopList[0])
            playsound(NextStation)
            playsound(destination)
            Announcer = False

        if doorCounter == 2 and Announcer == True:
            t.sleep(25)
            playsound(Welcome)
            playsound(operator)
            playsound(ServiceTo)
            playsound(destination)
            if LastStopList[0] in MainStation:
                playsound(CallingAt)
                playsound(destination)
                playsound(Only)
            playsound(NextStation)
            playsound(destination)
            playsound(Terminate)
            Announcer = False
        if doorCounter == 3:
            t.sleep(5)
            playsound(ThisIs)
            playsound(destination)
            playsound(Terminate)
            doorCounter = 0
            LastStop = False
FolderLabel = Label(gui, text="Announcement Folder:")
OriginLabel = Label(gui, text="Origin:")
DestinationLabel = Label(gui, text="Destination:")
OperatorLabel = Label(gui,text="Operator:")
FolderEntry = OptionMenu(gui,Fvar,*Folders, command=OnFupdate)
OriginEntry = OptionMenu(gui, ORvar, *Stations)
DestinationEntry = OptionMenu(gui, Dvar, *Destinations)
OperatorEntry = OptionMenu(gui, Ovar, *Operators)
StartupButton = Button(gui, command=Run, text="Set", bg="Blue", fg="White")

FolderEntry.config(width=15)
OriginEntry.config(width=15)
DestinationEntry.config(width=15)
OperatorEntry.config(width=15)

FolderLabel.grid(row=0,column=0,sticky=W,pady=2)
OriginLabel.grid(row=1,column=0,sticky=W,pady=2)
DestinationLabel.grid(row=2,column=0,sticky=W,pady=2)
OperatorLabel.grid(row=3, column=0,sticky=W,pady=2)
FolderEntry.grid(row = 0,column = 1, sticky= W, pady=2,padx=10) 
OriginEntry.grid(row = 1,column = 1, sticky= W, pady=2,padx=10)
DestinationEntry.grid(row = 2,column=1,sticky=W,pady=2, padx=10)
OperatorEntry.grid(row=3,column=1,sticky=W,pady=2,padx=10)
StartupButton.grid(row=4,column=1, sticky=E, pady=2, padx=10)

gui.mainloop()