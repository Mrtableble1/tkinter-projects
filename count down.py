import tkinter
import time

screen = tkinter.Tk()
screen.geometry("550x250")
screen.title("count down")

hour = tkinter.StringVar()
minute = tkinter.StringVar()
second = tkinter.StringVar()
hour.set("00")
minute.set("00")
second.set("00")

def click():
    h = int(entry1.get())
    m = int(entry2.get())
    s = int(entry3.get())
    ts = h*3600+m*60+s
    while ts > 0:
        ts -= 1
        hour.set(str(ts//3600))
        minute.set(str(ts%3600//60))
        second.set(str(ts%60))
        screen.update()
        time.sleep(1)
    
entry1 = tkinter.Entry(screen,textvariable=hour,bg ="white",fg = "black",width=10)
entry2 = tkinter.Entry(screen,textvariable=minute,bg ="white",fg = "black",width=10)
entry3 = tkinter.Entry(screen,textvariable=second,bg ="white",fg = "black",width=10)
button = tkinter.Button(screen,text = "set this count down",fg = "black",command = click)

entry1.grid(row =2,column =2,padx =20,pady = 20)
entry2.grid(row =2,column =3,padx =20,pady = 20)
entry3.grid(row =2,column =4,padx =15,pady = 20)
button.grid(row =7,column =3,padx =50,pady =80 )


screen.mainloop()