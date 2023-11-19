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

Ovar.set("Regional.mp3")
Dvar.set("Norrington.mp3")
Svar.set("HulmeHeath.mp3")
ORvar.set("Leaton.mp3")
Folders = os.listdir("Sounds")
Stations = os.listdir(os.path.join("Sounds", Fvar.get(), "stations"))
Destinations = os.listdir(os.path.join("Sounds", Fvar.get(), "dest"))
Operators = os.listdir(os.path.join("Sounds", Fvar.get(), "operators"))
def OnFupdate():
    print("updating")
    ORvar.set('')
    Dvar.set('')
    DestinationEntry['menu'].delete(0,'end')
    OriginEntry['menu'].delete(0,'end')
    OperatorEntry['menu'].delete(0,'end')
    Stations = os.listdir(os.path.join("Sounds", Fvar.get(), "stations"))
    Destinations = os.listdir(os.path.join("Sounds", Fvar.get(), "dest"))
    Operators = os.listdir(os.path.join("Sounds", Fvar.get(), "operators"))
    for choice in Destinations:
        DestinationEntry['menu'].add_command(label=choice, command=tkinter._setit(Dvar, choice))
    for choice in Operators:
        OperatorEntry['menu'].add_command(label=choice, command=tkinter._setit(Ovar, choice))
    for choice in Stations:
        OriginEntry["menu"].add_command(label=choice, command=tkinter._setit(ORvar, choice))


global icon
icon = PhotoImage(file="UI\\BRlogo.png")
window1.iconphoto(False, icon)
window1.title("BR Announcer")
global Continue

#Set Variables
def Startup():
    FolderLabel.config(text="Loading...")
    counter2 = 0
    doorCounter = 0
    Continue = "Yes"
    StopList = []
    LastStopList = []
    MainStation = ["Leaton.mp3", "Norrington.mp3", "FrestonJunction.mp3", "Newhurst.mp3", "BelmondGreen.mp3", "HulmeHeath.mp3"]
    Folder = os.path.join("Sounds", Fvar.get())
    operator = Ovar.get()
    origin = ORvar.get()
    destination = Dvar.get()
    sPath = os.path.join(Folder, 'stations')
    oPath = os.path.join(Folder, 'operators')
    dPath = os.path.join(Folder, 'dest')
    
    operator = AS.from_mp3(os.path.join(oPath, operator))
    destination = AS.from_mp3(os.path.join(dPath, destination))
    origin = ORvar.get()



    print(Folder)

    print("Loading...")
    Welcome = AS.from_mp3(Folder + "\Welcome.mp3")
    ServiceTo = AS.from_mp3(Folder + "\ServiceTo.mp3")
    NextStation = AS.from_mp3(Folder + "\\NextStation.mp3")
    Terminate = AS.from_mp3(Folder + "\\Terminate.mp3")
    Only = AS.from_mp3(Folder + "\\Only.mp3")
    CallingAt = AS.from_mp3(Folder + "\\CallingAt.mp3")
    And = AS.from_mp3(Folder + "\\And.mp3")
    ThisIs = AS.from_mp3(Folder + "\\ThisIs.mp3")

    def Announce(stop):
        sAudio = AS.from_mp3(os.path.join(sPath, stop))
        play(sAudio)
        
        if Calling == True and StopList.index(stop) == len(StopList) - 1:
            play(And)
            play(destination)
    print("Welcome!")
    LastStopList.append(origin)
    window1.destroy()
    window2 = Tk()
    icon = PhotoImage(file="UI\\BRlogo.png", master=window2)
    window2.iconphoto(False, icon)
    window2.title("BR Announcer")

    def ContinueFunction(): 
        Continue = Cvar.get()
        #Adding Stations
        def AddStation():
            station = Svar.get()
            StopList.append(station)
            ListLabel.config(text=StopList)
        def Done():
            window3.destroy()
        window2.destroy()
        if Continue == "Yes":
            Svar.set("Choose")
            window3 = Tk()
            window3.geometry('200x200')
            icon = PhotoImage(file="UI\\BRlogo.png", master=window3)
            window3.iconphoto(False, icon)
            window3.title("BR Announcer - Route Maker")
            StationLabel = Label(window3, text="Enter Station:")
            ListLabel = Label(window3, text="Stops Added:")
            StationEntry = OptionMenu(window3, Svar, *Stations)
            AddButton = Button(window3, text="Add Station", command=AddStation)
            DoneButton = Button(window3, text="Done", command=Done)

            DoneButton.grid(row=3,column=0,sticky=W,pady=2)
            StationLabel.grid(row=0,column=0,sticky=W,pady=2)
            StationEntry.grid(row=0, column=1,sticky=W,pady=2)
            ListLabel.grid(row=2, column=0,sticky=W,pady=2)
            AddButton.grid(row=1,column=0,sticky=W,pady=2)
            window3.mainloop()
        

    Cvar = StringVar()
    Cvar.set("Choose")
    ChoiceList = ["Yes", "No"]
    
    ContinueLabel = Label(window2, text="Does your route have more than 2 stops?")
    ContinueEntry = OptionMenu(window2,Cvar,*ChoiceList)
    ContinueButton = Button(window2, text="Confirm", command=ContinueFunction)
    ContinueEntry.config(width=50)

    ContinueLabel.grid(row=0,column=0,sticky=W,pady=2)
    ContinueEntry.grid(row=0,column=1,sticky=W,pady=2,padx=10)
    ContinueButton.grid(row=1,column=1,sticky=E,pady=2,padx=10)
        
    window2.mainloop()
    Calling = False
    #This Does announcements
    while len(StopList) > 0:
        if keyboard.is_pressed("t"):
            Announcer = True
            doorCounter = doorCounter + 1
        if doorCounter == 1 and Announcer == True:
            t.sleep(5)
            play(ThisIs)
            Announce(LastStopList[0])
            play(NextStation)
            Announce(StopList[0])
            Announcer = False
        if doorCounter == 2:
            counter2=0
            print(StopList[0])
            t.sleep(25)
            play(Welcome)
            play(operator)
            play(ServiceTo)
            play(destination)
            if LastStopList[0] in MainStation:
                Calling = True
                play(CallingAt)
                for x in StopList:
                    print(StopList.index(x))
                    print(len(StopList))
                    counter2 = counter2 + 1
                    Announce(x)
                Calling = False
            play(NextStation)
            print(StopList[0])
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

StartupButton = Button(window1, command=Startup, text="Set", bg="Blue", fg="White")

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
