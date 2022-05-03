import tkinter as tk
root = tk.Tk()
root.title("my title")
root.geometry('200x150')
root.configure(background='black')

from tkinter import *
parent = Tk()
caregory = Label(parent,text = "CATEGORY").grid(row = 0, column = 0)
cat  = Entry(parent).grid(row = 0, column = 1)
number = Label(parent,text = "QUANTITY").grid(row = 1, column = 0)
num = Entry(parent).grid(row = 1, column = 1)
submit = Button(parent, text = "Submit").grid(row = 4, column = 0)
parent.mainloop()




root.mainloop()
