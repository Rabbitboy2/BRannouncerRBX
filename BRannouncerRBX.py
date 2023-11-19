#import required modules
import time as t
from pydub import AudioSegment as AS
from pydub.playback import play 
import keyboard
from tkinter import *
import tkinter
import os
from pathlib import Path

window1 = Tk()
Fvar = StringVar()
Ovar = StringVar()
Dvar = StringVar()
Svar = StringVar()
ORvar = StringVar()
Fvar.set("tts")

def stemFile(file):
    stemmed = Path(file).stem
    return(stemmed)
Ovar.set("Regional")
Dvar.set("Norrington")
Svar.set("Hulme Heath")
ORvar.set("Leaton")
Folders = os.listdir("Sounds")
Stations = os.listdir(os.path.join("Sounds", Fvar.get(), "stations"))
Destinations = os.listdir(os.path.join("Sounds", Fvar.get(), "dest"))
Operators = os.listdir(os.path.join("Sounds", Fvar.get(), "operators"))
Stations = map(stemFile, Stations)
Destinations = map(stemFile, Destinations)
Operators = map(stemFile, Operators)

def OnFupdate():
    ORvar.set('')
    Dvar.set('')
    DestinationEntry['menu'].delete(0,'end')
    OriginEntry['menu'].delete(0,'end')
    OperatorEntry['menu'].delete(0,'end')
    Stations = os.listdir(os.path.join("Sounds", Fvar.get(), "stations"))
    Destinations = os.listdir(os.path.join("Sounds", Fvar.get(), "dest"))
    Operators = os.listdir(os.path.join("Sounds", Fvar.get(), "operators"))
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
window1.iconphoto(False, icon)
window1.title("BR Announcer")

#Set Variables
def Run():
    Stations = os.listdir(os.path.join("Sounds", Fvar.get(), "stations"))
    Destinations = os.listdir(os.path.join("Sounds", Fvar.get(), "dest"))
    Operators = os.listdir(os.path.join("Sounds", Fvar.get(), "operators"))
    Stations = map(stemFile, Stations)
    Destinations = map(stemFile, Destinations)
    Operators = map(stemFile, Operators)
    FolderLabel.config(text="Loading...")
    counter2 = 0
    doorCounter = 0
    StopList = []
    LastStopList = []
    MainStation = ["Leaton", "Norrington", "Freston Junction", "Newhurst", "Belmond Green", "Hulme Heath"]
    Folder = os.path.join("Sounds", Fvar.get())
    fConfirm.destroy()
    StartupButton.destroy()
    FolderLabel.destroy()
    Welcome = AS.from_mp3(Folder + "\Welcome.mp3")
    ServiceTo = AS.from_mp3(Folder + "\ServiceTo.mp3")
    NextStation = AS.from_mp3(Folder + "\\NextStation.mp3")
    Terminate = AS.from_mp3(Folder + "\\Terminate.mp3")
    Only = AS.from_mp3(Folder + "\\Only.mp3")
    CallingAt = AS.from_mp3(Folder + "\\CallingAt.mp3")
    And = AS.from_mp3(Folder + "\\And.mp3")
    ThisIs = AS.from_mp3(Folder + "\\ThisIs.mp3")
    Svar.set("Hulme Heath")
    icon = PhotoImage(file="UI\\BRlogo.png", master=window1)
    window1.iconphoto(False, icon)
    window1.title("BR Announcer - Route Maker")
    def AddStation():
        station = Svar.get()
        StopList.append(station)
        ListBox.insert(END, station)
        ListBox.see(ListBox.size())
    def RemoveLast():
        StopList.pop()
        ListBox.delete(ListBox.size() - 1)
    def Done():
        window1.destroy()
    StationLabel = Label(window1, text="Enter Station:")
    ListLabel = Label(window1, text="Stops Added:")
    ListBox = Listbox(window1)
    ListScroll = Scrollbar(window1)
    ListBox.config(yscrollcommand=ListScroll.set)
    ListScroll.config(command=ListBox.yview)
    Stations = os.listdir(os.path.join("Sounds", Fvar.get(), "stations"))
    Stations = map(stemFile, Stations)
    StationEntry = OptionMenu(window1, Svar, *Stations)
    StationEntry.config(width=15)
    AddButton = Button(window1, text="Add Station", command=AddStation)
    DelButton = Button(window1, text="Remove", command=RemoveLast)
    DoneButton = Button(window1, text="Done", command=Done)
    DoneButton.grid(row=7,column=0,sticky=W,pady=2)
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
    
    def Announce(stop):
        stopRoot = stop
        stop = stop + ".mp3"
        sAudio = AS.from_mp3(os.path.join(sPath, stop))
        play(sAudio)
        
        if Calling == True and StopList.index(stopRoot) == len(StopList) - 1:
            play(And)
            play(destination)
    window1.mainloop()
    operator = Ovar.get() + ".mp3"
    origin = ORvar.get()
    destination = Dvar.get() + ".mp3"
    sPath = os.path.join(Folder, 'stations')
    oPath = os.path.join(Folder, 'operators')
    dPath = os.path.join(Folder, 'dest')
    operator = AS.from_mp3(os.path.join(oPath, operator))
    destination = AS.from_mp3(os.path.join(dPath, destination))

    LastStopList.append(origin)
    Calling = False
    #This Does announcements
    while len(StopList) > 0:
        if keyboard.is_pressed("t"):
            Announcer = True
            doorCounter = doorCounter + 1
        if doorCounter == 1 and Announcer == True:
            t.sleep(0)
            play(ThisIs)
            Announce(LastStopList[0])
            play(NextStation)
            Announce(StopList[0])
            Announcer = False
        if doorCounter == 2:
            counter2=0
            t.sleep(0)
            play(Welcome)
            play(operator)
            play(ServiceTo)
            play(destination)
            if LastStopList[0] in MainStation:
                Calling = True
                for x in StopList:
                    counter2 = counter2 + 1
                    Announce(x)
                Calling = False
            play(NextStation)
            Announce(StopList[0])
            LastStopList.pop(0)
            LastStopList.append(StopList[0])
            StopList.pop(0)
            doorCounter = 0           
    LastStop = True
    while LastStop == True:
        if keyboard.is_pressed("t"):
            Announcer = True
            doorCounter = doorCounter + 1
        if doorCounter == 1 and Announcer == True:
            play(ThisIs)
            Announce(LastStopList[0])
            play(NextStation)
            play(destination)
            Announcer = False

        if doorCounter == 2 and Announcer == True:
            t.sleep(25)
            play(Welcome)
            play(operator)
            play(ServiceTo)
            play(destination)
            if LastStopList[0] in MainStation:
                play(CallingAt)
                play(destination)
                play(Only)
            play(NextStation)
            play(destination)
            play(Terminate)
            Announcer = False
        if doorCounter == 3:
            play(ThisIs)
            play(destination)
            play(Terminate)
            doorCounter = 0
            LastStop = False
FolderLabel = Label(window1, text="Announcement Folder:")
OriginLabel = Label(window1, text="Origin:")
DestinationLabel = Label(window1, text="Destination:")
OperatorLabel = Label(window1,text="Operator:")
FolderEntry = OptionMenu(window1,Fvar,*Folders)
OriginEntry = OptionMenu(window1, ORvar, *Stations)
DestinationEntry = OptionMenu(window1, Dvar, *Destinations)
OperatorEntry = OptionMenu(window1, Ovar, *Operators)
fConfirm = Button(window1, text="Set Folder", command=OnFupdate)
StartupButton = Button(window1, command=Run, text="Set", bg="Blue", fg="White")

FolderLabel.grid(row=0,column=0,sticky=W,pady=2)
OriginLabel.grid(row=1,column=0,sticky=W,pady=2)
DestinationLabel.grid(row=2,column=0,sticky=W,pady=2)
OperatorLabel.grid(row=3, column=0,sticky=W,pady=2)
FolderEntry.grid(row = 0,column = 1, sticky= W, pady=2,padx=10) 
fConfirm.grid(row = 0,column = 2, sticky= W, pady=2,padx=10) 
OriginEntry.grid(row = 1,column = 1, sticky= W, pady=2,padx=10)
DestinationEntry.grid(row = 2,column=1,sticky=W,pady=2, padx=10)
OperatorEntry.grid(row=3,column=1,sticky=W,pady=2,padx=10)
StartupButton.grid(row=4,column=1, sticky=E, pady=2, padx=10)

window1.mainloop()
