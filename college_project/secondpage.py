from tkinter import *
from PycharmProjects.college_project.firstpage import *
from PycharmProjects.basic.databasehelper import *
from PIL import ImageTk,Image
from tkinter import messagebox
class SecondPage(FirstPage):
    def __init__(self,root):
        super().__init__(root)
        self.add_widgets()
        #self.user_info()
    def user_info(self):
        username=self.e1.get()
        RollNo=self.e3.get()
        query ="Select * from User1 where UserName='%s' and UserRollNo ='%s'"
        #query ="Insert into User1(UserName,UserRollNo,UserClass,UserYear,User) Value('%s',%d,'%s','%s')"
        params = (username,RollNo)
        result2 = DataBaseHelper.get_all_data(query, params)
        #result3 = DataBaseHelper.execute_query(query,params)
        #result3=DataBaseHelper.execute_all_data_multiple_input(query,params)
        print(result2)
        print(username)
        print(RollNo)
    def get_screen(self):
        new_window=Toplevel()
        f = Frame(new_window, height=800, width=800)
        self.img1 = ImageTk.PhotoImage(Image.open("student1.jpg"))
        self.panel = Label(f, image=self.img1)
        self.panel.pack()
        self.m = Message(f, width=600, font="Roman 20 bold italic",
                            text="Enter Following Details", bg="white", relief=SOLID
                            , borderwidth=2)
        self.m.place(x=20,y=50)
        l7 = Label(f, width=20, text="Monday: ")
        self.e7 = Entry(f, width=30, fg='black', bg='white')
        self.e7.place(x=180,y=150)
        self.e7.focus_set()
        l8 = Label(f, width=20, text="Tuesday: ")
        self.e8 = Entry(f, width=30, fg='black', bg='white')
        self.e8.place(x=180, y=200)
        l9 = Label(f, width=20, text="Wednesday: ")
        self.e9 = Entry(f, width=30, fg='black', bg='white')
        self.e9.place(x=180, y=250)
        l10 = Label(f, width=20, text="Thursday: ")
        self.e10 = Entry(f, width=30, fg='black', bg='white')
        self.e10.place(x=180, y=300)
        l11 = Label(f, width=20, text="Friday: ")
        self.e11 = Entry(f, width=30, fg='black', bg='white')
        self.e11.place(x=180, y=350)
        l12 = Label(f, width=20, text="Saturday: ")
        self.e12 = Entry(f, width=30, fg='black', bg='white')
        self.e12.place(x=180, y=400)
        l7.place(x=20,y=150)
        l8.place(x=20,y=200)
        l9.place(x=20,y=250)
        l10.place(x=20, y=300)
        l11.place(x=20, y=350)
        l12.place(x=20, y=400)
        b3 = Button(f, text='Next', height=2, width=20,command = lambda : self.limit(new_window))
        b3.place(x=50,y=450)
        f.pack()
        self.panel.pack_propagate(0)
        f.pack_propagate(0)
    def calculate(self,result):
        ans=(result/42)*100
        ans=round(ans)
        min_res=75
        total_lectures=42
        lect=32-result
        lect1=21-result
        min_res1=50
        if(ans<50):
            atten2=ans
            my_message3="your are in critical defaulter , your attendance is",atten2,'%'
           # my_message4="you should atten %d lectures more to have attendance more than %d",lect,min_res
            messagebox.showinfo('Error',my_message3)
            #new_window1=Toplevel()
            #f1=Frame(new_window1,height=400,width=400)
            #msg=Message(f1,text=f'your weekly attendance is {ans}')
            #msg.config(bg='blue', font=('times', 24, 'italic'))
            #msg.pack()
            #f1.pack()
            #messagebox.showinfo('Error','Your are in critical defaulter list')
            print(f'you are in critical defaulter list')
            print(f'your week attendance is {ans}%')
            #print(f'you should attend {lect1} more lectures to have {min_res1}% attendance')
            print(f'you should attend {lect} more lectures to have {min_res}% attendance')
            return
        elif (ans>=50 and ans<75):
            atten=ans
            my_message="you are in defaulter list, your attendance is ",atten,"%"
            messagebox.showinfo('Error',my_message)
            print(f'You are in defaulter list!')
            print(f'your week attendance is {ans}%')
            print(f'you should attend {lect} more lectures to have {min_res}% attendance ')
            return
        else:
            atten1=ans
            my_message1="your attendance is ",atten1,"%"
            messagebox.showinfo('Success',my_message1)
            print(f"your week attendance is {ans}%")
    def limit(self,new_window):
        c=int(self.e7.get())
        d=int(self.e8.get())
        e=int(self.e9.get())
        i=int(self.e10.get())
        g=int(self.e11.get())
        h=int(self.e12.get())
        result=c+d+e+i+g+h
        if ((c or d or e or i or g or h )>7):
            messagebox.showerror('invalid entry','enter valid number of lectures')
        else:
            #new_window1=Toplevel()
            #f1=Frame(new_window1,height=600,width=700)
            b4=Button(new_window,text='Calculate attendance',height=2,width=20,command=lambda :self.calculate(result))
            b4.place(x=250,y=450)
            #f.pack()
            #messagebox.showinfo("valid entry", "click ok to check attendance")


    def add_widgets(self):
        l1 = Label(self.f, width=20, text="Name: ")
        self.e1 = Entry(self.f, width=30, fg='black', bg='white')
        l2 = Label(self.f, width=20, text="Class: ")
        #self.e2 = Entry(self.f, width=30, fg='black', bg='white')
        l3 = Label(self.f, width=20, text="Roll Number: ")
        l4 = Label(self.f, width=20, text="Year: ")
        self.e3 = Entry(self.f, width=30, fg='black', bg='white')
        self.e1.focus_set()
        l1.grid(row=1, column=1, padx=20, pady=20)
        l2.grid(row=2, column=1, padx=20, pady=20)
        l3.grid(row=3, column=1, padx=20, pady=20)
        l4.grid(row=4, column=1, padx=20, pady=20)
        self.e1.grid(row=1, column=2, padx=20, pady=20)
        #self.e2.grid(row=2, column=2, padx=20, pady=20)
        self.e3.grid(row=3, column=2, padx=20, pady=20)
        val1=StringVar()
        val1.set(' ')
        div=('A','B','C')
        self.o1=OptionMenu(self.f,val1,*div)
        self.o1.configure(width=15,bg='white')
        self.o1.place(x=210,y=75)
        val2=StringVar()
        val2.set(' ')
        y=('FE','SE','TE','BE')
        self.o2=OptionMenu(self.f,val2,*y)
        self.o2.configure(width=15,bg='white')
        self.o2.place(x=210,y=200)
        b1 = Button(self.f, text='Next', height=2, width=10,command=lambda :self.get_screen())
        b1.place(x=100,y=270)
        b2 = Button(self.f, text='Reset', height=2, width=10,command=lambda: self.reset())
        b2.place(x=200, y=270)
        b5 = Button(self.f, text='Admin page', height=2, width=10, command=lambda: self.user_info())
        b5.place(x=300, y=270)
        #self.user_info()
        self.f.pack()
        self.f.grid_propagate(0)
    # def submit(self,val1,val2):
    #     a=val1.get()
    #     b=val2.get()
    #     print(a,b)
    def reset(self):
        self.e1.delete(0,END)
        self.e3.delete(0,END)
root=Tk()
m=SecondPage(root)
root.mainloop()
