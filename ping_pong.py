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
    def __init__(self,padel1,padel2):
        self.ball= canvas.create_oval(0,0,50,50,fill="blue")
        self.bally = +4
        self.ballx = +4
        self.score1 = 0
        self.score2 = 0
        self.padel1 = padel1
        self.padel2 = padel2
    
    def draw(self):
        canvas.move(self.ball,self.ballx,self.bally)
        self.pos = canvas.coords(self.ball)
        self.pos1 = canvas.coords(self.padel1)
        self.pos2 = canvas.coords(self.padel2)

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
        

    def bounce(self):
        self.pos = canvas.coords(self.ball)
        self.pos1 = canvas.coords(self.padel1.padel)
        self.pos2 = canvas.coords(self.padel2.padel)
        if self.pos1[1] <= self.pos[3] and self.pos1[3] >= self.pos[1]:
            if self.pos1[0]<= self.pos[0] and self.pos1[2] >=self.pos[0]:
                self.ballx = 4

        if self.pos2[1] <= self.pos[3] and self.pos2[3] >= self.pos[1]:
            if self.pos2[0]<= self.pos[2] and self.pos2[0] >=self.pos[2]:
                self.ballx = -4



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
        self.changeY =-4


    def down(self,event):
        self.changeY =+4

    def move_up_down(self,keyup,keydown):
        canvas.bind_all(keyup,self.up)

        canvas.bind_all(keydown,self.down)




        

padel1 = Padel(10,250,30,350)
padel2 = Padel(770,250,790,350)

ball1 = Ball(padel1,padel2)

padel1.move_up_down('w','s')
padel2.move_up_down('<KeyPress-Up>','<KeyPress-Down>')

x = 0

while x == 0:
    ball1.draw()
    padel1.draw()
    padel2.draw()
    ball1.bounce()
    if ball1.score1 == 11:
        canvas.create_text(400,100,font=("Arial",50,"bold"),fill="white",text="player1 wins")
        break   

    if ball1.score2 == 11:
        canvas.create_text(400,100,font=("Arial",50,"bold"),fill="white",text="player2 wins")
        break
    screen.update_idletasks()
    screen.update()



screen.mainloop()