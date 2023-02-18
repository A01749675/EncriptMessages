# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:22:03 2022

@author: ikerf
"""

import tkinter as tk
import Encript as e


window = tk.Tk()
window.geometry("600x600")
window.configure(bg="black")
Label = tk.Label(window,text="Encript with the Boys",fg="green",bg="black",width=30,height=3,font=("TimesNewRoman",15))
Label.place(x=140,y=1)

def send():
    window = tk.Tk()
    window.geometry("600x400")
    window.configure(bg="black")
    Label1 = tk.Label(window, text="Message", fg="white", bg="black", width=10, height=3, font=("TimesNewRoman", 15))
    Label1.place(x=50, y=40)
    text = tk.Text(window, width=18, height=20, bg="gray", fg="blue")
    text.place(x=30, y=100)
    text2 = tk.Text(window, width=15, height=3, bg="gray", fg="blue")
    text2.place(x=200, y=200)
    def message():
        e.send_message(e.enctriptor(text.get("1.0","end-1c"),int(text2.get("1.0","end-1c"))))
        e.enctriptor(text.get("1.0", "end-1c"), int(text2.get("1.0", "end-1c")))

    Button = tk.Button(window,text="Encript and send",width=20,height=5,bg="green",fg="white",command = lambda m="F": message())
    Button.place(x=200,y=100)
def get():
    window = tk.Tk()
    window.geometry("700x400")
    window.configure(bg="black")
    Label1 = tk.Label(window, text="Message", fg="white", bg="black", width=10, height=3, font=("TimesNewRoman", 15))
    Label1.place(x=50, y=40)
    text = tk.Text(window, width=18, height=20, bg="gray", fg="blue")
    text.place(x=30, y=100)
    text2 = tk.Text(window, width=15, height=3, bg="gray", fg="blue")
    text2.place(x=200, y=200)
    def message():
        Label2 = tk.Label(window, text=e.solve(text.get("1.0","end-1c"),int(text2.get("1.0","end-1c"))), fg="white", bg="black", width=20, height=5,
                          font=("TimesNewRoman", 5))
        Label2.place(x=500, y=100)
    Button = tk.Button(window,text="Decript",width=20,height=5,bg="green",fg="white",command = lambda m="F": message())
    Button.place(x=200,y=100)

Button2 = tk.Button(window,text="Solve",width=20,height=5,bg="green",fg="white",command = lambda m="F":get() )
Button2.place(x=350,y=100)
Button1 = tk.Button(window,text="Send Message",width=20,height=5,bg="green",fg="white",command = lambda m="F": send())
Button1.place(x=50,y=100)




window.mainloop()