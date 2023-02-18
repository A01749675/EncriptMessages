# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:22:11 2022

@author: ikerf
"""

import random
import pywhatkit as p
from datetime import datetime
import pyautogui
from tkinter import *

def key():
    k = random.randint(1000,9999)
    return k

def enctriptor(text,key):
    new_text = ""
    k = str(key)
    n = len(k)
    count = 0
    for t in text:
        if t != " ":
            new_text+= chr(ord(t)+int(k[count-1]))
        else:
            new_text += " "
        if count < n:
            count+=1
        else:
            count+=0
    print(text)
    print(new_text)
    return new_text

def solve(text,key):
    new_text = ""
    k = str(key)
    n = len(k)
    count = 0
    for t in text:
        if t != " ":
            new_text+= chr(ord(t)-int(k[count-1]))
        else:
            new_text += " "
        if count < n:
            count+=1
        else:
            count+=0
    return new_text


def send_message(text):
    print(int(str(datetime.now())[14:16])+1)
    win = Tk() # Some Tkinter stuff
    screen_width = win.winfo_screenwidth() # Gets the resolution (width) of your monitor
    screen_height= win.winfo_screenheight()
    p.sendwhatmsg_to_group("Link to group",text,int(str(datetime.now())[11:13]),int(str(datetime.now())[14:16])+1,20)
    pyautogui.moveTo(screen_width * 0.694, screen_height* 0.964) # Moves the cursor the the message bar in Whatsapp
    pyautogui.click() # Clicks the bar
    pyautogui.press('enter') # Sends the message