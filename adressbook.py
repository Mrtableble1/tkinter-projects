import tkinter
import tkinter.messagebox
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

def showinfo(event):
    index = listbox.curselection()
    name =listbox.get(index)
    infobox = information[name]
    tkinter.messagebox.showinfo("bye","name:  "+name+"\naddress:  "+infobox[0]+"\nmobile:  "+infobox[1]+"\nemail: "+infobox[2]+"\nbirthday:  "+infobox[3])

def delete():
    index = listbox.curselection()
    name = listbox.get(index)
    del information[name]
    refresh()
    
def save():
    global information
    file1 = asksaveasfile()
    if file1 is not None:
        print(information,file=file1)
    else:
        tkinter.messagebox.showerror("np","file not saved")

def open():    
    global information
    file1 = askopenfile()
    if file1 is not None:
        items=file1.readlines()
        information = eval(items[0])
        refresh()

def edit():
    index = listbox.curselection()
    name = listbox.get(index)
    record = information[name]
    entry.insert(tkinter.END,name)
    entry1.insert(tkinter.END,record[0])
    entry2.insert(tkinter.END,record[1])
    entry3.insert(tkinter.END,record[2])
    entry4.insert(tkinter.END,record[3])


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
button= tkinter.Button(screen,text = "open",command= open)
button.place(x=300,y = 20)

button1= tkinter.Button(screen,text = "edit",command= edit)
button1.place(x=25,y = 500)

button2= tkinter.Button(screen,text = "delete",command= delete)
button2.place(x=150,y = 500)

button3= tkinter.Button(screen,text = "update",command= update)
button3.place(x=400,y = 500)

button4= tkinter.Button(screen,text = "save",command= save)
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
listbox.bind("<<ListboxSelect>>",showinfo)

screen.mainloop()