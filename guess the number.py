import tkinter
import tkinter.messagebox
import random

screen = tkinter.Tk()
screen.geometry("400x400")
screen.title("guess the number")
ans = random.randint(1,20)

def click():
    name = entry.get()
    tkinter.messagebox.showinfo("Want to play a game?","Hello "+name+" do you want to play a fun guessing game?")

def click1():
    guess = int(entry1.get())
    if guess > ans:
        tkinter.messagebox.showinfo("Bye","Your guess "+str(guess)+" is above then the number that I thought of")    

    if guess == ans:
        tkinter.messagebox.showinfo("good","Your guess "+str(guess)+" is the number that I thought of,You win!")    

    if guess < ans:
        tkinter.messagebox.showinfo("hello","Your guess "+str(guess)+" is lower then the number that I thought of")    



label1 = tkinter.Label(screen,text = "hello,Can you please tell me your name?",bg ="blue",fg = "white")
label2 = tkinter.Label(screen,text = "Guess the number:",bg ="blue",fg = "white")
entry = tkinter.Entry(screen,bg = "grey")
entry1 = tkinter.Entry(screen,bg = "grey")
button= tkinter.Button(screen,text = "ok",bg ="blue",fg = "black",command=click)
button1= tkinter.Button(screen,text = "guess",bg ="blue",fg = "black",command=click1)


label1.place(x= 0,y=50)
label2.place(x=0,y=150)
entry.place(x=0,y = 80)
entry1.place(x=120,y = 150)
button.place(x = 200,y=80)
button1.place(x = 300,y=150)





screen.mainloop()