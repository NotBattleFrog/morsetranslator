#morse_UI.py
import os 
import tkinter
from tkinter import *
import morse_translator

#UI setup
ui = tkinter.Tk()
ui.title("Morse Translator Version 1.1")
ui.geometry("400x150")
ui.resizable(width=False, height=False)

title = Label(ui, text="Morse Translator",font=("Arial Bold",30))
title.pack()

inputarea =  Entry(ui)
inputarea.pack(fill=X)

outputarea =Label(ui, text="Type something...")
outputarea.pack()

#function 
def clicked(i : int):
    if(i==1): # dot_clicked
         inputarea.insert(END,".")
    elif(i==2): # dash_clicked
        inputarea.insert(END,"-")
    elif(i==3): # space_clicked
        inputarea.insert(END," ")
    elif(i==4): # slash_clicked
        inputarea.insert(END,"|") 
    elif(i==5): # clear_clicked
        inputarea.delete(0, END)
        outputarea.configure(text= "Type something...")
    elif(i==6): # translate_clicked
       data = inputarea.get()
       if(data[0] == '.' or data[0] == '-'): # morse to text
           output = morse_translator.toWord(data)
           outputarea.configure(text= output)
           morse_translator.toSound(data)
       else: # text to morse
            output = morse_translator.toCode(data)
            outputarea.configure(text= output)
    elif(i==7): # copy_clicked
        data = outputarea.cget("text")
        ui.clipboard_clear()
        ui.clipboard_append(data)
    elif(i==8): # paste_clicked
        data = ui.clipboard_get()
        inputarea.insert(END,data)
    
#button
dot = Button(ui, text="Dot",command=lambda : clicked(1)).pack(padx=5,side=LEFT)
dash = Button(ui, text="Dash",command=lambda : clicked(2)).pack(padx=5,side=LEFT)
space = Button(ui, text="Space",command=lambda : clicked(3)).pack(padx=5,side=LEFT)
slash = Button(ui, text="Slash",command=lambda : clicked(4)).pack(padx=5,side=LEFT)
clear = Button(ui, text="Clear",command=lambda : clicked(5)).pack(padx=5,side=LEFT)
translate = Button(ui, text="Translate",command=lambda : clicked(6)).pack(padx=5,side=LEFT)
copy = Button(ui, text="Copy",command=lambda : clicked(7)).pack(padx=5,side=LEFT)
paste = Button(ui, text="Paste",command=lambda : clicked(8)).pack(padx=5,side=LEFT)
                                                                
#Run...
if __name__ == '__main__':
     ui.mainloop()






