import pyttsx3
from tkinter import *

root = Tk()
root.title("TTS")
root.geometry("350x400")
root.columnconfigure(0,weight=1)

ttsEntryvar = StringVar()
tts = Entry(root,width=50,textvariable=ttsEntryvar)
tts.grid()


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
engine.runAndWait()


def speak():
    try:
        text = tts.get()
        pyttsx3.speak(text)
    except:
        print("error")

btn = Button(root,text="Speak",width=10,bg="red",fg="white",command=speak())
btn.grid()
root.mainloop()
