# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 11:26:29 2020

@author: Ishika
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *
import tkinter.messagebox as tkMessageBox
from emotionrecogniser import final_emotion

# print(final_emotion)


root = Tk()
root.wm_title("MUSIC PLAYER")
root.minsize(500,500)


songs_list=[]
names = []

v =StringVar()
songlabel =Label(root,textvariable=v,width=80)
ind=0
counter=0

global ctrl
ctrl=0


def updatelabel():
    global ind
    global songname
    v.set(songs_list[ind])
    #return songname

def pausesong(event):
    global ctrl
    ctrl += 1
    if (ctrl%2!=0):
        pygame.mixer.music.pause()
    if(ctrl%2==0):
        pygame.mixer.music.unpause()

def playsong(event):
    pygame.mixer.music.play()


def nextsong(event):
    global ind
    ind += 1
    if (ind < counter):
        pygame.mixer.music.load(songs_list[ind])
        pygame.mixer.music.play()
    else:
        ind = 0
        pygame.mixer.music.load(songs_list[ind])
        pygame.mixer.music.play()
    try:
      updatelabel()
    except NameError:
        print("")

def prev_song(event):
    global ind
    ind -= 1
    pygame.mixer.music.load(songs_list[ind])
    pygame.mixer.music.play()
    try:
        updatelabel()
    except NameError:
        print("")


def stopsong(event):

    pygame.mixer.music.stop()
    
def mute(event):
    vol.set(0)



label = Label(root,text="Music Player")
label.pack()

listbox=Listbox(root,selectmode=MULTIPLE,width=100,height=20,bg="lightblue",fg="black")
listbox.pack(fill=X)


def choose_directory():
  global counter
  global ind
  directory = ""
  if final_emotion == "neutral":
      directory = "D:/codes/python codes/psc project/neutral"
  elif final_emotion == "angry":
      directory = "D:/codes/python codes/psc project/angry"
  elif final_emotion == "disgust":
      directory = "D:/codes/python codes/psc project/disgust"
  elif final_emotion == "happy":
      directory = "D:/codes/python codes/psc project/happy"
  elif final_emotion == "sad":
      directory = "D:/codes/python codes/psc project/sad"
  elif final_emotion == "surprise":
      directory = "D:/codes/python codes/psc project/surprise"
  elif final_emotion == "fear":
      directory = "D:/codes/python codes/psc project/fear"

  if(directory):
    counter=0
    ind=0
    #listbox.delete(0, END)
    del songs_list[:]
    del names[:]

    os.chdir(directory)

    for  files in os.listdir(directory):

        try:
         if files.endswith(".mp3"):

              realdir = os.path.realpath(files)
              audio = ID3(realdir)
              names.append(audio['TIT2'].text[0])
              songs_list.append(files)
        except:
            print(files+" is not a song")

    if songs_list == [] :
       okay=tkMessageBox.askretrycancel("No songs found","no songs")
       if(okay==True):
           choose_directory()

    else:
        listbox.delete(0, END)
        names.reverse()
        for things in names:
            listbox.insert(0, things)
        for i in songs_list:
            counter = counter + 1
        pygame.mixer.init()
        pygame.mixer.music.load(songs_list[0])

        pygame.mixer.music.play()
        try:
            updatelabel()
        except NameError:
            print("")
  else:
    return 1

try:
        choose_directory()
except WindowsError:
         print("thank you")


def calling(event):


 if(True):
    try:
        #pygame.mixer.music.stop()
        k=choose_directory()

    except WindowsError:
         print("Thank you!")

names.reverse()


songlabel.pack()


def show_value(self):
    i = vol.get()
    pygame.mixer.init(44100, -16,2,2048)

    pygame.mixer.music.set_volume(i)

vol = Scale(root,from_ = 10,to = 0,orient = VERTICAL ,resolution = 10,command = show_value)
vol.place(x=85, y = 380)
vol.set(10)

framemiddle =Frame(root,width=250,height=30)
framemiddle.pack()


bottom_frame =Frame(root,width=400,height=300)
bottom_frame.pack()

restartbutton = Button(bottom_frame,text="restart")
restartbutton.pack(side=LEFT)

mutebutton = Button(bottom_frame,text=u"\U0001F507")
mutebutton.pack(side=LEFT)

previousbutton = Button(bottom_frame,text="◄◄")
previousbutton.pack(side=LEFT)


playbutton = Button(bottom_frame,text="►")
playbutton.pack(side=LEFT)

stopbutton = Button(bottom_frame,text="■")
stopbutton.pack(side=LEFT)

nextbutton = Button(bottom_frame,text="►►")
nextbutton.pack(side=LEFT)


pausebutton = Button(bottom_frame,text="►/║║")
pausebutton.pack(side=LEFT)





mutebutton.bind("<Button-1>",mute)
restartbutton.bind("<Button-1>",calling)
playbutton.bind("<Button-1>",playsong)
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prev_song)
stopbutton.bind("<Button-1>",stopsong)
pausebutton.bind("<Button-1>",pausesong)

def when_closed():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        pygame.mixer.music.stop()
        root.destroy()

root.protocol("WM_DELETE_WINDOW", when_closed)


root.mainloop()