import tkinter
from tkinter.filedialog import *


screen = tkinter.Tk()
screen.geometry("400x400")
screen.title("Memorizer")

def add():
    text = entry.get()
    listbox.insert(tkinter.END,text)
    entry.delete(0,tkinter.END)

def delete():
    de = listbox.curselection()
    listbox.delete(de)

def save():
    file1 = asksaveasfile()
    if file1 is not None:
        items=listbox.get(0,tkinter.END)
        for item in items:
            print(item.strip(),file = file1)

def open():
    file1 = askopenfile()
    if file1 is not None:
        listbox.delete(0,tkinter.END)
        items=file1.readlines()
        for item in items:
            listbox.insert(tkinter.END,item.strip())

button1= tkinter.Button(screen,text = "OPEN",command= open,font=("verdana",15,"normal"))
button1.place(x=75,y = 0)

button2= tkinter.Button(screen,text = "DELETE",command= delete,font=("verdana",15,"normal"))
button2.place(x=150,y = 0)

button3= tkinter.Button(screen,text = "SAVE",command= save,font=("verdana",15,"normal"))
button3.place(x=235,y = 0)

button4= tkinter.Button(screen,text = "ADD",command= add,font=("verdana",15,"normal"))
button4.place(x=230,y = 40)

entry = tkinter.Entry(screen)
entry.place(x=20,y=40)

listbox = tkinter.Listbox(screen,width=40,height=17)
listbox.place(x=20,y=80)

screen.mainloop()