from tkinter import *
import sqlite3
from tkinter import messagebox

con=sqlite3.connect('database.db')
cur=con.cursor()

class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('600x650+450+50')
        self.title('Add People')
        self.resizable(False,False)

        ### Frames ###
        self.top=Frame(self,height=150,bg='white')
        self.top.pack(fill=X)
        self.bottom=Frame(self,height=500,bg='Yellow')
        self.bottom.pack(fill=X)

        ## Heading Images
        self.person_img=PhotoImage(file='icons/addperson.png')
        self.person_icon=Label(self.top,image=self.person_img,bg='white')
        self.person_icon.place(x=120,y=10)
        self.head=Label(self.top,text='Add people',fg='Blue',bg='White',font='Trebuchet 15 bold')
        self.head.place(x=280,y=60)

        ### Labels ###
        self.lbl_name=Label(self.bottom,text=' First Name : ',font='bold 12',bg='Yellow').place(x=60,y=10)
        self.lbl_sname=Label(self.bottom,text='Last Name : ',font='bold 12',bg='Yellow').place(x=60,y=70)
        self.lbl_email=Label(self.bottom,text='Email   : ',font='bold 12',bg='Yellow').place(x=60,y=130)
        self.lbl_phone=Label(self.bottom,text='Phone   : ',font='bold 12',bg='Yellow').place(x=60,y=190)
        self.lbl_Address=Label(self.bottom,text='Address : ',font='bold 12',bg='Yellow').place(x=60,y=310)

        ### Text Boxes ###
        self.entry_name=Entry(self.bottom,width=30)
        self.entry_name.insert(0,'Enter First Name')
        self.entry_name.place(x=180,y=10)

        self.entry_sname=Entry(self.bottom,width=30)
        self.entry_sname.insert(0,'Enter Surname')
        self.entry_sname.place(x=180,y=70)

        self.entry_email=Entry(self.bottom,width=30)
        self.entry_email.insert(0,'Enter Email')
        self.entry_email.place(x=180,y=130)

        self.entry_phone=Entry(self.bottom,width=30)
        self.entry_phone.insert(0,'Enter Phone')
        self.entry_phone.place(x=180,y=190)

        self.entry_address=Text(self.bottom,height=10,width=30,wrap=WORD)
        self.entry_address.place(x=180,y=250)
        #Button
        self.btn_addppl=Button(self.bottom,text='Add Details',width=10,font='bold 12',command=self.funcadd_people).place(x=280,y=420)
    
    def funcadd_people(self):
        name=self.entry_name.get()
        surname=self.entry_sname.get()
        email=self.entry_email.get()
        phone=self.entry_phone.get()
        address=self.entry_address.get(1.0,'end')
        if (name and surname and email and phone and address !=''):
            try:
                query='INSERT INTO "Persons" (person_name,person_surname,email,phone,address) VALUES (?,?,?,?,?)'
                cur.execute(query,(name,surname,email,phone,address))
                con.commit()
                messagebox.showinfo('Successful','Added to the Database')
                self.destroy()
            except:
                mb=messagebox.showerror('UnsuccessFul','Problem Adding to Database',icon='warning')   
        else:
            messagebox.showerror('Error','Fields Cannot Be Empty',icon='warning')

