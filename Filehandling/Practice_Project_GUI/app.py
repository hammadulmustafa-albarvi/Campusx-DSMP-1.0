from tkinter import * 
from tkinter import Tk
from database import *
from tkinter import messagebox
from myapi import *


class NLPApp:
    
    # First Time user Interface
    def __init__(self):
        self.tk = Tk()

        self.api = API()
        
        self.database = DataBase()
        
        self.tk.geometry('600x600')
        
        self.tk.title('NLPApp')
        
        self.login_interface()
        
        self.tk.mainloop()
        
      
     # Register Interface   
    def register_interface(self):
        for elements in self.tk.pack_slaves():
            elements.destroy()
        
        
        label1= Label(self.tk,text='NLPApp')
        label1.pack(pady=(30,30))
        label1.configure(font=('Arial',23))
        
        label2= Label(self.tk,text='Register')
        label2.pack(pady=(30,30))
        label2.configure(font=('Arial',17))
        
        label6= Label(self.tk,text='Enter Name')
        label6.pack(pady=(10,30))
        label6.configure(font=('Arial',13))
        
        self.name = Entry(self.tk,width=30)
        self.name.pack(ipadx=10)
        
        
        label3= Label(self.tk,text='Enter Email')
        label3.pack(pady=(10,30))
        label3.configure(font=('Arial',13))
        
        self.email = Entry(self.tk,width=30)
        self.email.pack(ipadx=10)
        
        label4= Label(self.tk,text='Enter Password')
        label4.pack(pady=(30,30))
        label4.configure(font=('Arial',13))        
        
        self.password = Entry(self.tk,width=30,show="*")
        self.password.pack(ipadx=10)
        
        register_button = Button(self.tk,text='Register',command=self.perform_registration,width=10,height=2)
        register_button.pack(pady=(10,10))
        
        label5= Label(self.tk,text='Already a member? Login Now')
        label5.pack(pady=(10,5))
        label5.configure(font=('Arial',10)) 
        
        login_button = Button(self.tk,text='Login Now',width=10,height=3,command=self.login_interface)
        login_button.pack(pady=(0,10))        
        
    # registration interface Backend
    def perform_registration(self):
        name = self.name.get()
        email = self.email.get()
        password = self.password.get()
        
        result = self.database.add_data(email,name,password)
        if result == 1:
            messagebox.showinfo('Success','Registration Done Successfully')
        else:
            messagebox.showerror('Error','Email Already exist')
        
        
        
    # login interface
    def login_interface(self):
        
        for elements in self.tk.pack_slaves():
            elements.destroy()

        label1= Label(self.tk,text='NLPApp')
        label1.pack(pady=(30,30))
        label1.configure(font=('Arial',23))
        
        label2= Label(self.tk,text='Login')
        label2.pack(pady=(30,30))
        label2.configure(font=('Arial',17))
        
        label3= Label(self.tk,text='Enter Email')
        label3.pack(pady=(10,30))
        label3.configure(font=('Arial',13))
        
        self.email = Entry(self.tk,width=30)
        self.email.pack(ipadx=10)
        
        label4= Label(self.tk,text='Enter Password')
        label4.pack(pady=(30,30))
        label4.configure(font=('Arial',13))        
        
        self.password = Entry(self.tk,width=30,show='*')
        self.password.pack(ipadx=10)
        
        login_button = Button(self.tk,text='Login',width=12,height=2,command=self.perform_login)
        login_button.pack(pady=(20,20))
        
        label5= Label(self.tk,text='Not a Member? Register Now')
        label5.pack(pady=(30,30))
        label5.configure(font=('Arial',13)) 
        
        register_button = Button(self.tk,text='Register Now',width=15,height=2,command=self.register_interface)
        register_button.pack(pady=(10,10))
        
    # login backend
    def perform_login(self):
        email = self.email.get()
        password = self.password.get()
        
        result = self.database.login(email,password)
        if result == 1:
            messagebox.showinfo('Success','You have logged in')
            self.home_interface()
        else:
            messagebox.showerror('Error','Incorrect Email/Password')
        
    
    def home_interface(self):
        
        for elements in self.tk.pack_slaves():
            elements.destroy()
         
        label1= Label(self.tk,text='NLPApp')
        label1.pack(pady=(30,30))
        label1.configure(font=('Arial',23))
         
         
        correction_button = Button(self.tk,text='Grammar and Spelling Correction',width=30,height=7,command=self.correction_gui)
        correction_button.pack(pady=(80,30))
        
        correction_button = Button(self.tk,text='Log Out',width=12,height=2,command=self.login_interface)
        correction_button.pack(pady=(30,10))
        
        
        
    def correction_gui(self):
        for elements in self.tk.pack_slaves():
            elements.destroy()
        
        label1= Label(self.tk,text='NLPApp')
        label1.pack(pady=(30,30))
        label1.configure(font=('Arial',23))
        
        label2= Label(self.tk,text='Grammar and Spelling Correction')
        label2.pack(pady=(30,30))
        label2.configure(font=('Arial',17))
        
        label3= Label(self.tk,text='Enter Text')
        label3.pack(pady=(10,30))
        label3.configure(font=('Arial',13))
        
        self.text = Entry(self.tk,width=30)
        self.text.pack(ipadx=10)
        
        correction = Button(self.tk,text='Correction',width=12,height=3,command=self.perform_correction)
        correction.pack(pady=(30,30))  
        
        self.result  = Label(self.tk,text='')
        self.result.pack()
        
        correction = Button(self.tk,text='Go Back',width=8,height=2,command=self.home_interface)
        correction.pack(pady=(30,30))  
        
        
    def perform_correction(self):
        text = self.text.get() 
        result = self.api.grammer_correction(text)
        data = result['correction'].split('.')
        text=''
        for i in data:
            text+=i+'\n'
        self.result['text'] = text
        
        
app = NLPApp()