from tkinter import *
import sqlite3
import addpeople
from tkinter import messagebox

con=sqlite3.connect('database.db')
cur=con.cursor()

'''
cur.execute('CREATE TABLE Persons(person_id INTEGER PRIMARY KEY AUTOINCREMENT,person_name TEXT,person_surname TEXT,email TEXT,phone TEXT,address TEXT)')
con.commit()
'''

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('600x650+450+50')
        self.title('My People')
        self.resizable(False,False)

        ### Frames  ###
        self.top=Frame(self,height=150,bg='WHITE')
        self.bottom=Frame(self,height=500,bg='Orange')
        self.top.pack(fill=X)
        self.bottom.pack(fill=X)

        ## Heading Images
        self.person_img=PhotoImage(file='icons/person_icon.png')
        self.person_icon=Label(self.top,image=self.person_img,bg='white')
        self.person_icon.place(x=120,y=10)
        self.head=Label(self.top,text='My People',fg='Blue',bg='White',font='Arial 15 bold')
        self.head.place(x=280,y=60)
        
        #List of people
        self.listbox=Listbox(self.bottom,width=60,height=31)
        self.listbox.grid(row=0,column=0,padx=(20,0))
        self.scrollbar=Scrollbar(self.bottom,orient=VERTICAL,command=self.listbox.yview)
        self.scrollbar.grid(row=0,column=1,sticky=N+S)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        #Query
        query="SELECT * FROM 'Persons'"
        people=cur.execute(query).fetchall()
        count=0
        for p in people:
            self.listbox.insert(count,str(p[0])+"."+str(p[1])+" "+str(p[2]))
            count+=1

        ### Buttons ###
        self.btn_Add=Button(self.bottom,width=12,text='Add',font='bold',command=self.func_add_people)
        self.btn_Add.grid(row=0,column=2,sticky=N,padx=20,pady=30)

        self.btn_update=Button(self.bottom,width=12,text='Update',font='bold',command=self.func_update)
        self.btn_update.grid(row=0,column=2,sticky=N,padx=20,pady=70)

        self.btn_delete=Button(self.bottom,width=12,text='Display',font='bold',command=self.func_display)
        self.btn_delete.grid(row=0,column=2,sticky=N,padx=20,pady=110)

        self.btn_delete=Button(self.bottom,width=12,text='Delete',font='bold',command=self.func_delete)
        self.btn_delete.grid(row=0,column=2,sticky=N,padx=20,pady=150)
    
    def func_add_people(self):
        add=addpeople.AddPeople()
        self.destroy()

    def func_update(self):
        global person_id
        selected_item=self.listbox.curselection()
        if len(selected_item)==0:
            messagebox.showerror('Error','Select 1 Person',icon='warning')
        else:
            person=self.listbox.get(selected_item)
            person_id=person.split('.')[0]
            Update()
            self.destroy()

    def func_display(self):
        global person_id
        selected_item=self.listbox.curselection()
        if len(selected_item)==0:
            messagebox.showerror('Error','Select 1 Person',icon='warning')
        else:
            person=self.listbox.get(selected_item)
            person_id=person.split('.')[0]
            Display()
            self.destroy()
    
    def func_delete(self):
        selected_item=self.listbox.curselection()
        if len(selected_item)==0:
            messagebox.showerror('Error','Select 1 Person',icon='warning')
        else:
            person=self.listbox.get(selected_item)
            person_id=person.split('.')[0]
            mbox=messagebox.askyesno('Delete','Do You really want to delete',icon='warning')
            if mbox==True:
                try:
                    cur.execute('DELETE FROM Persons WHERE person_id=?',(person_id))
                    con.commit()
                    messagebox.showinfo('Succesful','Selected Person deleted Sucessfully')
                    self.destroy()
                except:
                    messagebox.showerror('Error','Something Wrong Happened (Fill All the details if ot filled)',icon='Error')
            else:
                pass

class Update(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('600x650+450+50')
        self.title('Update Details')
        self.resizable(False,False)

        global person_id
        try:
            Details=cur.execute('SELECT * FROM Persons WHERE person_id=?',(person_id)).fetchall()
        except:
            messagebox.showerror('Error','Something wrong with DB')
        
        name=Details[0][1]
        surname=Details[0][2]
        email=Details[0][3]
        phone=Details[0][4]
        address=Details[0][5]
        ### Frames ###
        self.top=Frame(self,height=150,bg='white')
        self.top.pack(fill=X)
        self.bottom=Frame(self,height=500,bg='Yellow')
        self.bottom.pack(fill=X)

        ## Heading Images
        self.person_img=PhotoImage(file='icons/update.png')
        self.person_icon=Label(self.top,image=self.person_img,bg='white')
        self.person_icon.place(x=120,y=30)
        self.head=Label(self.top,text='Update Details',fg='Blue',bg='White',font='Trebuchet 15 bold')
        self.head.place(x=200,y=60)

        ### Labels ###
        self.lbl_name=Label(self.bottom,text=' First Name : ',font='bold 12',bg='Yellow').place(x=60,y=10)
        self.lbl_sname=Label(self.bottom,text='Last Name : ',font='bold 12',bg='Yellow').place(x=60,y=70)
        self.lbl_email=Label(self.bottom,text='Email   : ',font='bold 12',bg='Yellow').place(x=60,y=130)
        self.lbl_phone=Label(self.bottom,text='Phone   : ',font='bold 12',bg='Yellow').place(x=60,y=190)
        self.lbl_Address=Label(self.bottom,text='Address : ',font='bold 12',bg='Yellow').place(x=60,y=310)

        ### Text Boxes ###
        self.entry_name=Entry(self.bottom,width=30)
        self.entry_name.insert(0,name)
        self.entry_name.place(x=180,y=10)

        self.entry_sname=Entry(self.bottom,width=30)
        self.entry_sname.insert(0,surname)
        self.entry_sname.place(x=180,y=70)

        self.entry_email=Entry(self.bottom,width=30)
        self.entry_email.insert(0,email)
        self.entry_email.place(x=180,y=130)

        self.entry_phone=Entry(self.bottom,width=30)
        self.entry_phone.insert(0,phone)
        self.entry_phone.place(x=180,y=190)

        self.entry_address=Text(self.bottom,height=10,width=30,wrap=WORD)
        self.entry_address.insert(1.0,address)
        self.entry_address.place(x=180,y=250)
        #Button
        self.btn_addppl=Button(self.bottom,text='Update Details',width=12,font='bold 12',command=self.func_update).place(x=280,y=420)

    def func_update(self):
        name=self.entry_name.get()
        surname=self.entry_sname.get()
        email=self.entry_email.get()
        phone=self.entry_phone.get()
        address=self.entry_address.get(1.0,'end')
        try:
            query='Update Persons SET person_name=?,person_surname=?, email=?, phone=?, address=? WHERE person_id=?'
            cur.execute(query,(name,surname,email,phone,address,person_id))
            con.commit()
            messagebox.showinfo('Success','Updated Successfully')
            self.destroy()
        except:
            messagebox.showerror('Error','Something Wrong happned',icon='warning')
        
class Display(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('600x650+450+50')
        self.title('Update Details')
        self.resizable(False,False)

        global person_id
        try:
            Details=cur.execute('SELECT * FROM Persons WHERE person_id=?',(person_id)).fetchall()
        except:
            messagebox.showerror('Error','something wrong with DB')
       
        name=Details[0][1]
        surname=Details[0][2]
        email=Details[0][3]
        phone=Details[0][4]
        address=Details[0][5]

        ### Frames ###
        self.top=Frame(self,height=150,bg='white')
        self.top.pack(fill=X)
        self.bottom=Frame(self,height=500,bg='Yellow')
        self.bottom.pack(fill=X)

        ## Heading Images
        self.person_img=PhotoImage(file='icons/person.png')
        self.person_icon=Label(self.top,image=self.person_img,bg='white')
        self.person_icon.place(x=120,y=40)
        self.head=Label(self.top,text='Person Details',fg='Blue',bg='White',font='Trebuchet 15 bold')
        self.head.place(x=200,y=60)

        ### Labels ###
        self.lbl_name=Label(self.bottom,text=' First Name : ',font='bold 12',bg='Yellow').place(x=60,y=10)
        self.lbl_sname=Label(self.bottom,text='Last Name : ',font='bold 12',bg='Yellow').place(x=60,y=70)
        self.lbl_email=Label(self.bottom,text='Email   : ',font='bold 12',bg='Yellow').place(x=60,y=130)
        self.lbl_phone=Label(self.bottom,text='Phone   : ',font='bold 12',bg='Yellow').place(x=60,y=190)
        self.lbl_Address=Label(self.bottom,text='Address : ',font='bold 12',bg='Yellow').place(x=60,y=310)

        ### Text Boxes ###
        self.entry_name=Entry(self.bottom,width=30)
        self.entry_name.insert(0,name)
        self.entry_name.config(state='disabled')
        self.entry_name.place(x=180,y=10)

        self.entry_sname=Entry(self.bottom,width=30)
        self.entry_sname.insert(0,surname)
        self.entry_sname.config(state='disabled')
        self.entry_sname.place(x=180,y=70)

        self.entry_email=Entry(self.bottom,width=30)
        self.entry_email.insert(0,email)
        self.entry_email.config(state='disabled')
        self.entry_email.place(x=180,y=130)

        self.entry_phone=Entry(self.bottom,width=30)
        self.entry_phone.insert(0,phone)
        self.entry_phone.config(state='disabled')
        self.entry_phone.place(x=180,y=190)

        self.entry_address=Text(self.bottom,height=10,width=30,wrap=WORD)
        self.entry_address.insert(1.0,address)
        self.entry_address.config(state='disabled')
        self.entry_address.place(x=180,y=250)
