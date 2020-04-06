from tkinter import*

root = Tk()

pic = PhotoImage(file = 'jntu.png')
label = Label(root, image=pic)
label.pack()

root.mainloop()
