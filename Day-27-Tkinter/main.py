from tkinter import Tk, Label, Button, Entry
from typing import Sized

# Screen
screen = Tk()
screen.title("My first GUI python program")
screen.minsize(width=500, height=300)
screen.config(padx=20, pady=20)

# Label
label = Label(text="I am a label", font=("Arial", 24, "bold"))
label.grid(row=0, column=0)
label.config(text="New text", padx=50, pady=50)

#Button
def button_clicked():
    label.config(text=input.get())
    
    
button = Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)

button = Button(text="New Button", command=button_clicked)
button.grid(row=0, column=2)

#Entry
input = Entry(width=10)
input.grid(row=2, column=3)

    
screen.mainloop()