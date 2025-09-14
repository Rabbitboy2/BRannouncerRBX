# BRannouncerRBX
This is an announcer program for the roblox game 'British Railway'.

Dependecies:

-Python (Must be added to PATH)

-playsound (use installDependencies.bat to install)

-keyboard (use installDependencies.bat to install)

To run this program when all the dependecies are installed, run the run.bat file included.

This program has multiple features including...

-Customisable sound sets (found in the Sounds folder)

-A tkinter based dropdown interface

-All station names (as of V1.3). This list is no longer updated due to the devs adding an announcement system in game. 


For creating your own sound sets use the folder structure:  

BRannouncer

>UI>BRlogo.png
>
>Sounds
>>SoundSetName

>>>dest

>>>info

>>>operators

>>>stations

>>>extra

dest folder is for destination sound files

operators folder is for operator sound files

stations folder is for station sound files

extra folder is for extra sound files that can be played by using y key instead of t

info folder is for all of the other sound files (These ones are required)


Required sound files (stored in info folder): And.mp3, CallingAt.mp3, NextStation.mp3, Only.mp3, ServiceTo.mp3, Terminate.mp3, ThisIs.mp3, Welcome.mp3
