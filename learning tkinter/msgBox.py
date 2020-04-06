from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Today\'s SNAP', 'Ajay is AWESOME')

answer = tkinter.messagebox.askquestion('Question 1','Will you Agree?')

if answer == 'yes':
    print('Congratulations!!!')

root.mainloop()
