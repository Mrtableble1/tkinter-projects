import tkinter
import tkinter.ttk

screen = tkinter.Tk()
screen.geometry("500x800")
screen.title("table")



def click():
    number = int(cb1.get())
    rang = int(multi.get())

    tabel = ""
    for i in range(1,rang+1):
        tabel = tabel+str(number)+" x "+str(i)+" = "+str(number*i)+"\n"
    label2.config(text = tabel)



label2 = tkinter.Label(screen,text ="")
label2.place(x =200 ,y =200)

label1 = tkinter.Label(screen,text = "mathematical table",font=("verdana",20,"normal"))
label1.place(x= 150,y=20)

numbers = []
for i in range(1,51):
    numbers.append(i)
cb1 = tkinter.ttk.Combobox(screen)
cb1.place( x= 150,y = 100)
cb1["values"]=numbers

multi = tkinter.IntVar()

rb1 = tkinter.Radiobutton(screen,text = "10",variable=multi,value=10)
rb1.place(x =400,y=70)

rb2 = tkinter.Radiobutton(screen,text = "20",variable=multi,value=20)
rb2.place(x =400,y=100)

rb3 = tkinter.Radiobutton(screen,text = "30",variable=multi,value=30)
rb3.place(x =400,y=130)


button= tkinter.Button(screen,text = "Generate",command= click)
button.place(x=200,y = 150)

label1 = tkinter.Label(screen,text = "Number and Range")
label1.place(x=27,y= 100)









screen.mainloop()