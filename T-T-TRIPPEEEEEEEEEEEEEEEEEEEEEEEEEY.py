from Tkinter import *
from time import sleep

class FOgre:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.trip1 = "trip1.gif"
        self.trip2 = "trip2.gif"
        self.image = PhotoImage(file=self.trip1) 
        self.label = Label(frame, image=self.image)
        self.label.bind("<Button-1>", self.Trap)
        self.label.pack()

    def Trap(self, event):
        self.image.config(file=self.trip2)
        self.label.bind("<Button-1>", self.Trayp)

    def Trayp(self, event):
        self.image.config(file=self.trip1)
        self.label.bind("<Button-1>", self.Trap)
        
        
        
        
        
        
        



root = Tk()
window = FOgre(root)
root.mainloop()
