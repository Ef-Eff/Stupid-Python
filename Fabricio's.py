from Tkinter import *
from random import randint
'''
        self.= Button(text="", command=self.)
        self..grid(row=0, column=, padx=2, pady=2)
'''

class UltimateKode:
    def __init__(self, master):
        frame = Frame(master, bg="black")
        frame.grid()

        self.anti_vowel = Button(text="Anti-Vowel", command=self.Anti_Vowel)
        self.anti_vowel.grid(row=0, padx=2, pady=2)

        self.censor = Button(text="Censor", command=self.Censor)
        self.censor.grid(row=0, column=1, padx=2, pady=2)

        self.fibonacci = Button(text="Fibonacci", command=self.Fibonacci)
        self.fibonacci.grid(row=0, column=2, padx=2, pady=2)

        self.factorial= Button(text="Factorial", command=self.Factorial)
        self.factorial.grid(row=0, column=3, padx=2, pady=2)

        self.reversed = Button(text="Reversed", command=self.Reversed)
        self.reversed.grid(row=0, column=4, padx=2, pady=2)

        self.scrabble = Button(text="Scrabble?!", command=self.Scrabble)
        self.scrabble.grid(row=1, column=0, padx=2, pady=2)

        self.ch = Button(text="Clicker Heroes", command=self.Clicker_Heroes)
        self.ch.grid(row=1, column=1, padx=2, pady=2)

    def Clicker_Heroes(self):
        self.w8 = Tk(className=" Clicker Heroes")
        self.CHlabel1 = Label(self.w8, text="DPS Calc for clicking")
        self.CHlabel1.pack()
        self.CHEntry = Entry(self.w8)
        self.CHEntry.pack()
        self.CHEntry1 = Entry(self.w8)
        self.CHEntry1.pack()

        self.CHlabel2 = Label(self.w8, font="System")
        self.CHlabel2.pack(side=BOTTOM)

        self.CHcontents = IntVar(self.w8)
        self.CHcontents1 = IntVar(self.w8)
        self.CHEntry["textvariable"] = self.CHcontents
        self.CHEntry1["textvariable"] = self.CHcontents1
        self.CHEntry1.bind('<Key-Return>', self.aClicker_Heroes)

    def aClicker_Heroes(self, event):
        self.CHa = 100 - self.CHcontents.get()
        self.CHb = self.CHcontents.get() * self.CHcontents1.get()
        self.CHc = self.CHa + self.CHb
        self.CHgg = str(self.CHc)
        self.CHlabel2.config(text=self.CHgg)
           

    def Scrabble(self):
        self.Scscore = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
        self.w7 = Tk(className=" Scrabble")
        self.Sclabel1 = Label(self.w7, text="Dats rite fam, calculate the Scrabble score for any word!")
        self.Sclabel1.pack()
        self.ScEntry = Entry(self.w7)
        self.ScEntry.pack()

        self.Sclabel2 = Label(self.w7, font="System", text="9")
        self.Sclabel2.pack(side=BOTTOM)

        self.Sccontents = StringVar(self.w7)
        self.Sccontents.set("Memes")
        self.ScEntry["textvariable"] = self.Sccontents
        self.ScEntry.bind('<Key-Return>', self.aScrabble)

    def aScrabble(self, event):
        self.Scword = self.Sccontents.get()
        self.Scs = 0
        self.Scword = self.Scword.lower()
        for everything in self.Scword:
            self.Scs += self.Scscore[everything]
        self.Sclabel2.config(text=self.Scs)

             
    def Reversed(self):
        self.w5 = Tk(className=" Reversed")
        self.Revlabel1 = Label(self.w5, text="Input any word or sentence to have it reversed!")
        self.Revlabel1.pack()
        self.RevEntry = Entry(self.w5)
        self.RevEntry.pack()

        self.Revlabel2 = Label(self.w5, font="System", text="elpmaxE")
        self.Revlabel2.pack(side=BOTTOM)

        self.Revcontents = StringVar(self.w5)
        self.Revcontents.set("Example")
        self.RevEntry["textvariable"] = self.Revcontents
        self.RevEntry.bind('<Key-Return>', self.aReversed)

    def aReversed(self, event):
        self.Revt = ""
        self.Revtext = self.Revcontents.get()
        self.Revg = len(self.Revtext) - 1
        for every in self.Revtext:
            self.Revt += self.Revtext[self.Revg]
            self.Revg -= 1
        self.Revlabel2.config(text=self.Revt)
        

    def Factorial(self):
        self.w4 = Tk(className=" Factorial")
        self.Faclabel1 = Label(self.w4, text="Input any number to see the factorial.")
        self.Faclabel1.pack()
        self.FacEntry = Entry(self.w4)
        self.FacEntry.pack()

        self.Faclabel2 = Label(self.w4, font="System")
        self.Faclabel2.pack(side=BOTTOM)

        self.Faccontents = IntVar(self.w4)
        self.Faccontents.set("")
        self.FacEntry["textvariable"] = self.Faccontents
        self.FacEntry.bind('<Key-Return>', self.aFactorial)

    def aFactorial(self, event):
        self.Factotal = 1
        self.Facn = self.Faccontents.get()
        if self.Faccontents.get() < 1:
            self.Faclabel2.config(text=self.Factotal)
        else:
            while self.Facn != 1:
                self.Factotal *= self.Facn
                self.Facn -= 1
        self.Faclabel2.config(text=self.Factotal)


    def Censor(self):
        self.w3 = Tk(className=" Censor")
        self.Clabel1 = Label(self.w3, text="Type any sentence below.")
        self.Clabel1.pack()
        self.CEntry = Entry(self.w3)
        self.CEntry.pack()
        self.Clabel2 = Label(self.w3, text="Now type the word you want censored.")
        self.Clabel2.pack()
        self.CEntry2 = Entry(self.w3)
        self.CEntry2.pack()

        self.Clabel3 = Label(self.w3, font="System", text="Just like ****")
        self.Clabel3.pack(side=BOTTOM)

        self.Ccontents = StringVar(self.w3)
        self.Ccontents.set("Just like this")
        self.CEntry["textvariable"] = self.Ccontents
        self.Ccontents2 = StringVar(self.w3)
        self.Ccontents2.set("this")
        self.CEntry2["textvariable"] = self.Ccontents2
        self.CEntry2.bind("<Key-Return>", self.aCensor)
        
    def aCensor(self, event):
        self.Cword = self.Ccontents2.get()
        self.Ca = len(self.Cword)
        self.Ctext = self.Ccontents.get()
        self.Cl = self.Ctext.split()
        self.Ck = 0
        for e in self.Cl:
            if e != self.Cword:
                self.Ck += 1
                continue
            elif e == self.Cword:
                self.Cl[self.Ck] = "*" * self.Ca
                self.Ck += 1
        self.Clabel3.config(text=" ".join(self.Cl))
    
        
    def Anti_Vowel(self):
        self.w2 = Tk(className=" Anti-Vowel")
        self.avlabel1 = Label(self.w2, text="Enter any sentence, and the vowels will be removed.")
        self.avlabel1.pack()
        self.avEntry = Entry(self.w2)
        self.avEntry.pack()

        self.avlabel2 = Label(self.w2, font="System", text="xmpl")
        self.avlabel2.pack(side=BOTTOM)

        self.avcontents = StringVar(self.w2)
        self.avcontents.set("Example")
        self.avEntry["textvariable"] = self.avcontents
        self.avEntry.bind('<Key-Return>', self.aAnti_Vowel)

    def aAnti_Vowel(self, event):
        self.avt = ""
        self.avtext = self.avcontents.get()
        for i in self.avtext:
            if i == "a" or i == "A" or \
               i == "e" or i == "E" or \
               i == "i" or i == "I" or \
               i == "o" or i == "O" or \
               i == "u" or i == "U":
                continue
            else:
                self.avt += i
        self.avlabel2.config(text=self.avt)
        self.w2.mainloop()        


    def Fibonacci(self):
        self.w2 = Tk(className=" Fibonacci")
        self.FibLabel = Label(self.w2, text="Enter the highest number you want it calculated to.")
        self.FibLabel.pack()
        self.fibEntry = Entry(self.w2)
        self.fibEntry.pack()

        self.fiblabel = Label(self.w2, font="System")
        self.fiblabel.pack(side=BOTTOM)

        self.fibc = IntVar(self.w2)
        self.fibc.set(0)
        self.fibEntry["textvariable"] = self.fibc
        self.fibEntry.bind('<Key-Return>', self.aFibonacci)

    def aFibonacci(self, event):
        self.fiba, self.fibb = 0, 1
        self.fibx = self.fibc.get()
        self.fibt = ""
        while self.fibb <= self.fibx:
            self.fibt += str(self.fibb) + " "
            self.fiblabel.config(text=self.fibt)
            self.fiba, self.fibb = self.fibb, self.fiba+self.fibb
        self.w2.mainloop()
        
'''        
    def xxx(self):
        w
'''
       
root = Tk(className=" Ultimate Program Fam")
placeholder = UltimateKode(root)
root.mainloop()










