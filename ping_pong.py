import tkinter
from tkinter.colorchooser import askcolor


screen = tkinter.Tk()
screen.geometry("800x600")
screen.title("ping pong")

canvas = tkinter.Canvas(screen,width=800,height=600,bg="black")
canvas.place(x=0,y=0)

canvas.create_line(400,0,400,600,width=3,fill="white")
canvas.create_oval(300,200,500,400,outline="white",width=3)

class Ball():
    def __init__(self):
        self.ball= canvas.create_oval(0,0,50,50,fill="blue")

ball = Ball()

class Padel():
    def __init__(self,x0,y0,x1,y1):
        self.padel= canvas.create_rectangle(x0,y0,x1,y1,fill="yellow")

pade1 = Padel(10,250,30,350)
padel2 = Padel(770,250,790,350)
screen.mainloop()