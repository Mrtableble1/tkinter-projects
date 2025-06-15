import tkinter
import random

screen = tkinter.Tk()
screen.geometry("400x400")
screen.title("fun game of tik tak toe!")

def open(selected):
    if selected in button:
        button.remove(selected)
        selected.config(text = "X")
        chosen = random.choice(button)
        button.remove(chosen)
        chosen.config(text="o")



#buttons

button1= tkinter.Button(screen,command=lambda:open(button1),padx = 30,pady = 30)
button1.place(x=20,y = 20)

button2= tkinter.Button(screen,command=lambda:open(button2),padx = 30,pady = 30)
button2.place(x=120,y = 20)

button3= tkinter.Button(screen,command=lambda:open(button3),padx = 30,pady = 30)
button3.place(x=220,y = 20)

button4= tkinter.Button(screen,command=lambda:open(button4),padx = 30,pady = 30)
button4.place(x=20,y = 120)

button5= tkinter.Button(screen,command=lambda:open(button5),padx = 30,pady = 30)
button5.place(x=120,y = 120)

button6= tkinter.Button(screen,command=lambda:open(button6),padx = 30,pady = 30)
button6.place(x=220,y = 120)

button7= tkinter.Button(screen,command=lambda:open(button7),padx = 30,pady = 30)
button7.place(x=20,y = 220)

button8= tkinter.Button(screen,command=lambda:open(button8),padx = 30,pady = 30)
button8.place(x=120,y = 220)

button9= tkinter.Button(screen,command=lambda:open(button9),padx = 30,pady = 30)
button9.place(x=220,y = 220)

button = [button1,button2,button3,button4,button5,button6,button7,button8,button9]

screen.mainloop()