import tkinter

screen = tkinter.Tk()
screen.geometry("800x800")
screen.title("starting tkinter")

def click():
    screen.config(background = "blue")


label = tkinter.Label(screen,text = "hello person",bg ="blue",fg = "white",padx = 70,pady = 70)

entry = tkinter.Entry(screen,bg ="blue",fg = "black")

entry1 = tkinter.Entry(screen,bg ="blue",fg = "black")

button = tkinter.Button(screen,text = "please click me",fg = "black",padx = 70,pady = 70,command = click)



label.place(x =132,y = 142)

entry.place(x=382,y = 223)

entry1.place(x=200,y = 500)

button.place(x = 400,y =569)





screen.mainloop()