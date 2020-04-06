from tkinter import *


def doNothing():
    print("I dont do ANYTHING..")

root = Tk()

#-------MAIN MENU------------------
menu = Menu(root)
root.config(menu= menu)

subMenu = Menu(menu)
menu.add_cascade(label = "File", menu = subMenu)

subMenu.add_command(label = "New Project..", command = doNothing)
subMenu.add_command(label = "New..", command = doNothing)
subMenu.add_separator()
subMenu.add_command(label = "Exit", command = doNothing)

editMenu = Menu(menu)
editMenu.add_cascade(label = "Edit",menu = editMenu)
editMenu.add_command(label = "Redo", command = doNothing)


#---------TOOL BAR-----------------
toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text = "InsertImage", command = doNothing)
insertButt.pack(side = LEFT, padx = 2, pady = 2)
printButt = Button(toolbar, text = "Print", command = doNothing)
printButt.pack(side = LEFT, padx = 2, pady = 2)


toolbar.pack(side = TOP, fill = X)

#--------STATUS BAR-----------------------
status = Frame(root, text = "Preparing to do nothing", bd = 1, relief = SUNKEN, anchor = W)
status.pack(side = BOTTOM, fill = X)


root.mainloop()

