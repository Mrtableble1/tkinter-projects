import tkinter
import random

screen = tkinter.Tk()
screen.geometry("800x400")
screen.title("rock,paper")

chose = ["rock","paper","scissors"]

csc = 0
psc = 0

def click(ps):
    global csc,psc
    label5.config(text = "You Selected - "+ps)

    cs = random.choice(chose)
    label7.config(text = "Computer Selected - "+cs)

    if ps == cs:
        label1.config(text = "No one won the round!",fg="black")

    if ps == "rock" and cs =="scissors" or ps == "paper" and cs =="rock" or ps == "scissors" and cs == "paper":
        label1.config(text = "Player Wins!",fg="green")
        psc +=1
        label6.config(text = "Player Score "+str(psc))
        

    if ps == "scissors" and cs =="rock" or ps == "rock" and cs =="paper" or ps == "paper" and cs == "scissors":
        label1.config(text = "Computer Wins!",fg="red")
        csc +=1
        label8.config(text = "Computer Score "+str(csc))
        

label = tkinter.Label(screen,text ="Rock,Paper,Scissors",font=("verdana",25,"normal"))
label.place(x= 270,y=20)

label1 = tkinter.Label(screen,text = "You won!",fg="green",font=("verdana",15,"normal"))
label1.place(x = 350,y = 70)

label3 = tkinter.Label(screen,text = "Your Options:")
label3.place(x = 50,y = 130)

button = tkinter.Button(screen,text = "Rock",fg = "black",font=("verdana",15,"normal"),command = lambda:click("rock"))
button.place(x=200,y = 160)

button1 = tkinter.Button(screen,text = "paper",fg = "black",font=("verdana",15,"normal"),command =lambda:click("paper"))
button1.place(x=400,y = 160)

button2 = tkinter.Button(screen,text = "scissors",fg = "black",font=("verdana",15,"normal"),command = lambda:click("scissors"))
button2.place(x=600,y = 160)

label4 = tkinter.Label(screen,text = "score:")
label4.place(x = 50,y = 200)

label5 = tkinter.Label(screen,text = "You selected ")
label5.place(x = 200,y = 230)

label6 = tkinter.Label(screen,text = "player score: ")
label6.place(x = 500,y = 230)

label7 = tkinter.Label(screen,text = "computer selected ")
label7.place(x = 200,y = 260)

label8 = tkinter.Label(screen,text = "computer score: ")
label8.place(x = 500,y = 260)

screen.mainloop()