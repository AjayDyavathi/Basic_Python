from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1=(topFrame, text = "Button1", foreground="red")
button2=(topFrame, text="Button2", fg="blue")
button3=(topFrame, text="Button3", fg="green")
button4=(bottomFrame, text="Button4", fg="purple")

'''
button1.pack()
button2.pack()
button3.pack()
button4.pack()

'''
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)


root.mainloop()
