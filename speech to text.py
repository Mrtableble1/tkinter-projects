import tkinter
import speech_recognition as sr


screen = tkinter.Tk()
screen.geometry("500x400")
screen.title("speech to text")

def click():
    r = sr.Recognizer()
    #recognizer object
    with sr.Microphone() as source:
        print("start speaking")
        audio = r.listen(source)
        try:
            text2=r.recognize_google(audio)
        except:
            text2 ="Sorry I could not understand"
        text.delete(0,tkinter.END)
        text.insert(tkinter.END,text2)

label = tkinter.Label(screen,text = "speech to text",bg ="grey",fg = "white",padx = 150,pady = 70,font=("verdana",30,"normal"))
label.place(x =0,y = 0)

text = tkinter.Text(screen,width=40,height=8)
text.place(x=100,y = 200)

button = tkinter.Button(screen,text = "record",fg = "black",background = "red",padx = 70,pady = 20,command=click)
button.place(x = 150,y =330)



screen.mainloop()