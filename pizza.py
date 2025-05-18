import tkinter
import tkinter.ttk


screen = tkinter.Tk()
screen.geometry("600x400")
screen.title("Best pizza")

def click():
    number = cb1.get()
    rang = multi.get()
    food = int(cb2.get())

    order = ""
    order = "you order is "+str(number)+" "+str(rang)+" size "+str(food)
    label4.config(text=order)

label1 = tkinter.Label(screen,text = "welcome to pizza hut!",font=("verdana",20,"normal"))
label1.place(x= 190,y=20)

label2 = tkinter.Label(screen,text = "chose your fav pizza")
label2.place(x= 25,y=100)

label3 = tkinter.Label(screen,text = "chose your quantiy")
label3.place(x= 25,y=150)

label4 = tkinter.Label(screen,text ="")
label4.place(x=200,y=300)

button= tkinter.Button(screen,text = "order",command= click)
button.place(x=250,y = 250)

food = ["veg ","veg ","veg ","veg ","veg ","non-veg","non-veg","non-veg","non-veg","non-veg"]
cb1 = tkinter.ttk.Combobox(screen)
cb1.place( x= 200,y = 100)
cb1["values"]=food

numbers = []
for i in range(1,11):
    numbers.append(i)
cb2 = tkinter.ttk.Combobox(screen)
cb2.place( x= 200,y = 150)
cb2["values"]=numbers

multi = tkinter.StringVar()

rb1 = tkinter.Radiobutton(screen,text = "S",variable=multi,value="Small")
rb1.place(x =500,y=100)

rb2 = tkinter.Radiobutton(screen,text = "M",variable=multi,value="Medium")
rb2.place(x =500,y=150)

rb3 = tkinter.Radiobutton(screen,text = "L",variable=multi,value="Large")
rb3.place(x =500,y=200)


screen.mainloop()