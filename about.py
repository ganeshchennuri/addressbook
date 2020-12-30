from tkinter import *

class About(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('550x500+350+50')
        self.title('About Us')
        self.resizable(False,False)

        self.Frr=Frame(self,height=500,bg='Orange')
        self.Frr.pack(fill=BOTH)
        about=Label(self.Frr,text='This is About Us Page\n AdddressBook App with sqlite Database\nDeveloped using Tkinter',fg='Black',bg='Orange',font='Times 15 bold')
        about.place(x=100,y=200)
    