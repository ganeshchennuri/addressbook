from tkinter import *
from datetime import date
import mypeople,addpeople,about

class APP(object):
    def __init__(self,mainn):
        self.mainn=mainn
        ### Frames ###
        self.top=Frame(mainn,height=150,bg='WHITE')
        self.bottom=Frame(mainn,height=400,bg='green')
        self.top.pack(fill=X)
        self.bottom.pack(fill=X)

        ## Heading Images and Date
        '''
        script_dir = os.path.dirname(__file__)
        rel_path='book.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        '''
        self.book_icon=PhotoImage(file='icons/book.png')
        self.book_img=Label(self.top,image=self.book_icon,bg='white')
        self.book_img.place(x=120,y=10)
        self.head=Label(self.top,text='My Address Book App',fg='Red',bg='White',font='Arial 12 bold')
        self.head.place(x=260,y=60)
        self.date=Label(self.top,text='Today\'s Date : '+str(date.today()),fg='Red',bg='white',font='bold 11')
        self.date.place(x=350,y=5)
        
        
        ### Buttons ###
        self.btn1_icon=PhotoImage(file='icons/man.png')
        self.btn2_icon=PhotoImage(file='icons/add.png')
        self.btn3_icon=PhotoImage(file='icons/info.png')
        self.BtnMyPeople=Button(self.bottom,text='  My People  ',font='bold 12',
                                image=self.btn1_icon,compound=LEFT,command=self.openMyPeople).place(x=220,y=40)
        self.BtnAddPeople=Button(self.bottom,text=' Add People ',font='bold 12',image=self.btn2_icon,compound=LEFT,
                                 command=self.add_people).place(x=220,y=100)
        self.BtnAbout=Button(self.bottom,text='    About        ',font='bold 12',image=self.btn3_icon,compound=LEFT,
                             command=self.about).place(x=220,y=160)
        
    def openMyPeople(self):
        people=mypeople.MyPeople()

    def add_people(self):
        add_peep=addpeople.AddPeople()

    def about(self):
        about.About() 
def main():
    root=Tk()
    app=APP(root)
    root.title('Address Book')
    root.geometry('550x500+350+50')
    root.resizable(False,False)
    root.mainloop()

if __name__ == "__main__":
    main()