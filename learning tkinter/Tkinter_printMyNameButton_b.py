'''
from tkinter import *

root = Tk()

def printName():
    print("Hello!, My name is Ajay Dyavathi")

button1 = Button(root, text = "Print my name", command = printName)
button1.pack()
'''

    
from tkinter import *

root = Tk()

def printName(event):
    print("Hey!!\nMy name is Ajay Dyavathi!!!")

button1 = Button(root, text = "My Name")
button1.bind("<Button-1>", printName)
button1.pack()

root.mainloop()

