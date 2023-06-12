# import required modules
import tkinter as tk
from tkinter import *
import randfacts


# function to add facts
def move():
    facts = randfacts.get_fact(True)
    c = "*) "
    label = Label(root, text=c + facts)
    label.pack()


# function to close window
def destroy():
    root.destroy()


# driver code
root = tk.Tk()

# adjust window
root.config(bg="red")
root.geometry("1200x400")
# add buttons
button = tk.Button(root, text="Click here for Facts", command=move)
button2 = tk.Button(root, text="Clear and quit", command=destroy)
button.pack()
button2.pack()

root.mainloop()
