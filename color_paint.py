import tkinter
from tkinter.colorchooser import askcolor

class Paint():
    def __init__(self):
        self.screen = tkinter.Tk()
        self.screen.geometry("800x800")
        self.screen.title("color paint")
        self.button1= tkinter.Button(self.screen,text = "pen",command= self.usepen)
        self.button1.place(x=50,y = 20)
        self.button2= tkinter.Button(self.screen,text = "color",command= self.selectcolor)
        self.button2.place(x=200,y = 20)
        self.button3= tkinter.Button(self.screen,text = "brush",command = self.usebrush)
        self.button3.place(x=350,y = 20)
        self.button4= tkinter.Button(self.screen,text = "easer",command = self.useeraser)
        self.button4.place(x=500,y = 20)
        self.scale= tkinter.Scale(self.screen,from_=1,to=10,orient="horizontal")
        self.scale.place(x=650,y=15)
        self.canvas = tkinter.Canvas(self.screen,width=800,height=750,bg="white")
        self.canvas.place(x=0,y=70)
        self.setup()
        self.screen.mainloop()
    def setup(self):
        self.pencolor = "black"
        self.pensize = 1
        self.eraseron = "off"
        self.oldx = None
        self.oldy = None
        self.canvas.bind("<B1-Motion>",self.draw)
        self.canvas.bind("<ButtonRelease-1>",self.reset)
        self.selectedbutton = self.button1

    def draw(self,event):
        color = self.pencolor
        self.pensize = self.scale.get()
        if self.eraseron == "off":
            color = self.pencolor
        else:
            color = "white"
        if self.oldx and self.oldy:
            self.canvas.create_line(self.oldx,self.oldy,event.x,event.y,width=self.pensize,fill=color,smooth=True,capstyle=tkinter.ROUND)
        self.oldx = event.x
        self.oldy = event.y
    def reset(self,event):
        self.oldx = None
        self.oldy = None
    def selectcolor(self):
            self.eraseron = "off"
            self.pencolor = askcolor(color = self.pencolor)[1]
    def usepen(self):
        eraseron = "off"
        self.selectedbutton.config(relief=tkinter.RAISED)
        self.button1.config(relief=tkinter.SUNKEN)
        self.selectedbutton = self.button1
    def usebrush(self):
        eraseron = "off"
        self.selectedbutton.config(relief=tkinter.RAISED)
        self.button3.config(relief=tkinter.SUNKEN)
        self.selectedbutton = self.button3
    def useeraser(self):
        eraseron = "on"
        self.selectedbutton.config(relief=tkinter.RAISED)
        self.button4.config(relief=tkinter.SUNKEN)
        self.selectedbutton = self.button4

    
            






Paint()