from tkinter import *


class AjaysButtons:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text = "Print message", command = self.printMessage)
        self.printButton.pack(side = LEFT)

        self.quitButton = Button(frame, text = "Quit", command = frame.quit)
        self.quitButton.pack(side = LEFT)

        def printMessage(self):
            print("Yayy!!This is Working!!!")



root = Tk()
a = AjaysButtons(root)
root.mainloop()
