#morse_UI.py
import os 
import tkinter
from tkinter import *
import morse_translator

#UI setup
ui = tkinter.Tk()
ui.title("Morse Translator Version 1.0")
ui.geometry("600x150")

title = Label(ui, text="Morse Translator",font=("Arial Bold",30))
title.grid(column=0, row=1)

inputarea =  Entry(ui,width=50)
inputarea.grid(column=0, row=2)

outputarea =Label(ui, text="Type something...")
outputarea.grid(column=0, row=3)

#function
def dot_clicked():
    inputarea.insert(END,".")
def dash_clicked():
    inputarea.insert(END,"-")
def clear_clicked():
    inputarea.delete(0, END)
    outputarea.configure(text= "Type something...")
def translate_clicked():
    data = inputarea.get()
    if(data[0] == '.' or data[0] == '-'): # morse to text
       output = morse_translator.toWord(data)
       morse_translator.toSound(data)
       outputarea.configure(text= output)
    else: # text to morse
        output = morse_translator.toCode(data)
        outputarea.configure(text= output)
def copy_clicked():
      data = outputarea.cget("text")
      ui.clipboard_clear()
      ui.clipboard_append(data) 
    
#button
dot = Button(ui, text="Dot",command=dot_clicked)
dot.grid(column=1, row=2)

dash = Button(ui, text="Dash",command=dash_clicked)
dash.grid(column=2, row=2)

clear = Button(ui, text="Clear",command=clear_clicked)
clear.grid(column=3, row=2)

translate = Button(ui, text="Translate",command=translate_clicked)
translate.grid(column=4, row=2)

copy = Button(ui, text="Copy to clipboard",command=copy_clicked)
copy.grid(column=0, row=4)

#Run...
ui.mainloop()





