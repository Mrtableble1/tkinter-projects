import tkinter
import calendar

screen = tkinter.Tk()
screen.geometry("800x600")
screen.title("calender")

def click():
    year = int(entry.get())
    calender = calendar.calendar(year)

    screen1 = tkinter.Tk()
    screen1.geometry("600x500")
    screen1.title(str(year))
    text = tkinter.Text(screen1,width= 100,height=150)
    text.insert(tkinter.END,calender)

    text.pack()

    screen1.mainloop()




label = tkinter.Label(screen,text = "calender",bg ="grey",fg = "white",padx = 400,pady = 70)
entry = tkinter.Entry(screen,bg ="grey",fg = "black")
label1 = tkinter.Label(screen,text = "enter year",bg ="green",fg = "white",padx = 70,pady = 30)
button = tkinter.Button(screen,text = "exit",fg = "black",background = "red",padx = 70,pady = 20)
button1 = tkinter.Button(screen,text = "show calender",fg = "black",background= "red",padx = 70,pady = 20,command=click)


entry.place(x=320,y = 240)
label.place(x =0,y = 0)
label1.place(x =320,y = 160)
button.place(x = 315,y =300)
button1.place(x = 300,y =400)


screen.mainloop()