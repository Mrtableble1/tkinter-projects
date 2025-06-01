import tkinter
import tkinter.ttk

screen = tkinter.Tk()
screen.geometry("400x400")
screen.title("color changer")

color = ["white","black","grey","blue","red","orange","purple","pink","green"]
cb1 = tkinter.ttk.Combobox(screen)
cb1.place( x= 183,y = 0)
cb1["values"]=color

def add():
    text = cb1.get()
    listbox.insert(tkinter.END,text)
    cb1.delete(0,tkinter.END)

def delete():
    de = listbox.curselection()
    listbox.delete(de)

def change_color():
    index = listbox.curselection()
    colors = listbox.get(index)
    screen.config(background = colors)  

button= tkinter.Button(screen,text = "DELETE",command= delete)
button.place(x=60,y = 370)

button1= tkinter.Button(screen,text = "ADD",command= add)
button1.place(x=0,y = 370)

button2= tkinter.Button(screen,text = "change background ",command= change_color)
button2.place(x=0,y = 345)

listbox = tkinter.Listbox(screen,width=20,height=20)
listbox.place(x=0,y=0)

screen.mainloop()