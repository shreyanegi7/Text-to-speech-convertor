from tkinter import *
from gtts import gTTS
 
  
import os
 

root = Tk()

 

frame1 = Frame(root,
               bg = "lightPink",
               height = "150")
 

frame1.pack(fill = X)
 
 
frame2 = Frame(root,
               bg = "lightgreen",
               height = "750")
frame2.pack(fill=X)
 
 
label = Label(frame1, text = "Text to Speech",
              font = "bold, 30",
              bg = "yellow")
 
label.place(x = 180, y = 70)
 
 
entry = Entry(frame2, width = 45,
              bd = 4, font = 14)
 
entry.place(x = 130, y = 52)
entry.insert(0, "")
 

def play():

    language = "en"
    input_text =entry.get()
    for_in rage(10)
    print("input Text:", input_text)
 
 
    myobj = gTTS(text_ =  input_text, lang=language,
                lang = language,
                slow = False)
 
 
 
    myobj.save("convert.wav")
    os.system("convert.wav")

btn = Button(frame2, text = "SUBMIT",
             width = "15", pady = 10,
             font = "bold, 15",
             command = play, bg='green')
 
btn.place(x = 250,
          y = 130)
  
root.title("text_to_speech_convertor")
 

root.geometry("650x550+350+200")
 

root.mainloop()

for(i<n,i<;i)