import tkinter

screen = tkinter.Tk()
screen.geometry("800x400")
screen.title("temprature converter")
screen.config(bg="grey")

def click():
    temp = float(entry.get())
    far = 1.8*temp+32
    label3.config(text = "fahrenheit is "+str(far))
    
    

label = tkinter.Label(screen,text = "celsius-->Fahrenheit",font=("verdana",50,"normal"),bg ="grey",fg = "white",)
label1 = tkinter.Label(screen,text = "please enter the celsuis here->",bg ="grey",fg = "white")
entry = tkinter.Entry(screen,bg = "grey")
label2 = tkinter.Label(screen,text = "please enter only numbers",bg ="grey",fg = "white")
button= tkinter.Button(screen,text = "convert",bg ="green",fg = "black",command= click)
label3 = tkinter.Label(screen,text = "",font=("verdana",25,"normal"),bg ="grey",fg = "white")


label.place(x= 150,y = 0)
label1.place(x = 250,y = 120)
entry.place(x = 450,y = 120)
label2.place(x = 450,y = 150)
button.place(x=400,y = 200)
label3.place(x = 300,y = 240)


screen.mainloop()