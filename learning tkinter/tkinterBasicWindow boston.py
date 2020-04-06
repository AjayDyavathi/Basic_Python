'''from tkinter import *

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
	#self.master = master
root = Tk()

app = Window(root)

root.mainloop()
'''

from tkinter import *
root = Tk()
label = Label(root, text="Hi Ajay,\nWelcome to Tkinter..")
label.pack()
root.mainloop()
