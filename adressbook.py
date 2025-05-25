import tkinter
from tkinter.filedialog import *

screen = tkinter.Tk()
screen.geometry("600x600")
screen.title("adress booking")

information = {}

def update():
    name = entry.get()
    address = entry1.get()
    mobile = entry2.get()
    email = entry3.get()
    birthday = entry4.get()
    information[name]=[address,mobile,email,birthday]
    refresh()
    entry.delete(0,tkinter.END)
    entry1.delete(0,tkinter.END)
    entry2.delete(0,tkinter.END)
    entry3.delete(0,tkinter.END)
    entry4.delete(0,tkinter.END)


def refresh():
    names = information.keys()
    listbox.delete(0,tkinter.END)
    for name in names:
        listbox.insert(tkinter.END,name)


def click():
    print(7)

#labels
label1 = tkinter.Label(screen,text = "My address book:")
label1.place(x= 150,y=20)

label2 = tkinter.Label(screen,text = "name:")
label2.place(x= 300,y=80)

label3 = tkinter.Label(screen,text = "Address:")
label3.place(x= 300,y=150)

label4 = tkinter.Label(screen,text = "Moblie:")
label4.place(x= 300,y=250)

label5 = tkinter.Label(screen,text = "email:")
label5.place(x= 300,y=350)

label6 = tkinter.Label(screen,text = "birthday:")
label6.place(x= 300,y=450)


#buttons
button= tkinter.Button(screen,text = "open",command= click)
button.place(x=300,y = 20)

button1= tkinter.Button(screen,text = "edit",command= click)
button1.place(x=25,y = 500)

button2= tkinter.Button(screen,text = "delete",command= click)
button2.place(x=150,y = 500)

button3= tkinter.Button(screen,text = "update",command= update)
button3.place(x=400,y = 500)

button4= tkinter.Button(screen,text = "save",command= click)
button4.place(x=280,y = 500)

#entry
entry = tkinter.Entry(screen)
entry.place(x=400,y=80)

entry1 = tkinter.Entry(screen)
entry1.place(x=400,y=150)

entry2 = tkinter.Entry(screen)
entry2.place(x=400,y=250)

entry3 = tkinter.Entry(screen)
entry3.place(x=400,y=350)

entry4 = tkinter.Entry(screen)
entry4.place(x=400,y=450)



listbox = tkinter.Listbox(screen,width=23,height=24)
listbox.place(x=20,y=80)

screen.mainloop()