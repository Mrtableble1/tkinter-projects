import tkinter
from tkinter.colorchooser import askcolor


screen = tkinter.Tk()
screen.geometry("800x600")
screen.title("ping pong")

canvas = tkinter.Canvas(screen,width=800,height=600,bg="black")
canvas.place(x=0,y=0)

canvas.create_line(400,0,400,600,width=3,fill="white")
canvas.create_oval(300,200,500,400,outline="white",width=3)
score = canvas.create_text(400,50,font=("Arial",50,"bold"),fill="white",text="0:0")


class Ball():
    def __init__(self):
        self.ball= canvas.create_oval(0,0,50,50,fill="blue")
        self.bally = +4
        self.ballx = +4
        self.score1 = 0
        self.score2 = 0
        
    
    def draw(self):
        canvas.move(self.ball,self.ballx,self.bally)
        self.pos = canvas.coords(self.ball)

        if self.pos[0] <= 0:
            self.ballx =+ 4
            self.score2 +=1

        if self.pos[1] <= 0:
            self.bally =+ 4

        if self.pos[2] >= 800:
            self.ballx =- 4
            self.score1 +=1

        if self.pos[3] >= 600:
            self.bally =- 4
        
        canvas.itemconfigure(score,text=str(self.score1)+":"+str(self.score2))


ball1 = Ball()

class Padel():
    def __init__(self,x0,y0,x1,y1):
        self.padel= canvas.create_rectangle(x0,y0,x1,y1,fill="yellow",)
        self.changeY = 0
    def draw(self):
        canvas.move(self.padel,0,self.changeY)
        self.pos = canvas.coords(self.padel)
        if self.pos[1] <=0:
            self.changeY = 0

        if self.pos[3] >=600:
            self.changeY = 0
        
    def up(self,event):
        changeY =-4


    def down(self,event):
        changeY =+4

    def move_up_down(self,keyup,keydown):
        canvas.bind_all(keyup,self.up)

        canvas.bind_all(keydown,self.down)




        

padel1 = Padel(10,250,30,350)
padel2 = Padel(770,250,790,350)

padel1.move_up_down('w','s')

x = 0

while x == 0:
    ball1.draw()
    padel1.draw()
    padel2.draw()
    screen.update_idletasks()
    screen.update()


screen.mainloop()