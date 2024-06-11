from tkinter import *

def on_button_click():
    print("Button clicked")


root = Tk() 
b = Button(root, text="Click me", command=on_button_click ) 
b.pack() 

root.mainloop() 