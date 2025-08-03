import tkinter
from gtts import gTTS
import os

screen = tkinter.Tk()
screen.geometry("500x400")
screen.title("text to speech")

def click():
    text = entry.get()
    audio = gTTS(text,lang = "en",slow = False)
    audio.save("speech.mp3")



label = tkinter.Label(screen,text = "text to speech",bg ="grey",fg = "white",padx = 150,pady = 70,font=("verdana",30,"normal"))
label.place(x =0,y = 0)

entry = tkinter.Entry(screen)
entry.place(x=160,y = 250)

button = tkinter.Button(screen,text = "submit",fg = "black",background = "red",padx = 70,pady = 20,command=click)
button.place(x = 150,y =300)




screen.mainloop()