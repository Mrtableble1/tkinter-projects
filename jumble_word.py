import tkinter
import random
import tkinter.messagebox

screen = tkinter.Tk()
screen.geometry("400x400")
screen.title("jumble words")



words =["butterlfy","snail","chair","table","bedroom","guests","elephant","computer","printer","weather"]
word = ""
score = 0

def items():
    global word,score
    word = random.choice(words)
    word_list = list(word)
    random.shuffle(word_list)
    jumbeld_word = ''.join(word_list)
    label3.config(text=jumbeld_word)
    words.remove(word)



def checking():
    global word,score
    pword = entry.get() 
    entry.delete(0,tkinter.END)
    if pword == word:
        score+=1
        label2.config(text=str(score))
        tkinter.messagebox.showinfo("dw","You got a point!")
        items()

    


label1 = tkinter.Label(screen,text = "jumbled word game!",font=("verdana",20,"normal"))
label1.place(x= 100,y=20)

label2 = tkinter.Label(screen,text = "0")
label2.place(x= 20,y=350)

label3 = tkinter.Label(screen,text = "0",font=("verdana",20,"normal"))
label3.place(x= 170,y=100)

button= tkinter.Button(screen,text = "reset",command= checking,font=("verdana",15,"normal"))
button.place(x=150,y = 250)

button1= tkinter.Button(screen,text = "check",command= checking,font=("verdana",15,"normal"))
button1.place(x=150,y = 200)

entry = tkinter.Entry(screen)
entry.place(x=100,y=150)

items()

screen.mainloop()