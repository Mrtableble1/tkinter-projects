import tkinter



class Paint():
    def __init__(self):
        self.screen = tkinter.Tk()
        self.screen.geometry("800x800")
        self.screen.title("color changer")
        self.button1= tkinter.Button(self.screen,text = "pen")
        self.button1.place(x=50,y = 20)
        self.button2= tkinter.Button(self.screen,text = "color")
        self.button2.place(x=200,y = 20)
        self.button3= tkinter.Button(self.screen,text = "brush")
        self.button3.place(x=350,y = 20)
        self.button4= tkinter.Button(self.screen,text = "easer")
        self.button4.place(x=500,y = 20)
        self.scale= tkinter.Scale(self.screen,from_=1,to=10,orient="horizontal")
        self.scale.place(x=650,y=15)
        self.canvas = tkinter.Canvas(self.screen,width=800,height=750,bg="white")
        self.canvas.place(x=0,y=70)
        self.screen.mainloop()



Paint()