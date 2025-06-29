import tkinter
import tkinter.messagebox

screen = tkinter.Tk()
screen.geometry("400x400")
screen.title("fun game of tik tak toe!")

def open(selected):
    global turn
    if selected in button:
        button.remove(selected)
        selected.config(text = turn)
        winner()
        if turn == "X":
            turn = "o"
        elif turn == "o":
            turn = "X"

turn = "X"

def winner():
    for wc in winning_combos:
        if wc[0]["text"] == "X" and wc[1]["text"] == "X" and wc[2]["text"] == "X":
            tkinter.messagebox.showinfo("wsp","Player1 wins!")

        elif wc[0]["text"] == "o" and wc[1]["text"] == "o" and wc[2]["text"] == "o":
            tkinter.messagebox.showinfo("wsp","Player2 wins!")

    if len(button) == 0:
        tkinter.messagebox.showinfo("hello","It's a tie!")


seconds = 0
def timer():
    global seconds
    seconds = seconds+1
    label.config(text=seconds)
    label.after(1000,timer)

#buttons

label = tkinter.Label(screen,text = seconds)
label.place(x= 150,y=350)

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
winning_combos = [[button1,button2,button3],[button4,button5,button6],[button7,button8,button9],[button1,button4,button7],[button2,button5,button8],[button3,button6,button9],[button1,button5,button9],[button3,button5,button7]]
timer()
screen.mainloop()