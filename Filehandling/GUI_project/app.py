from mydb import *
from tkinter import *
from myapi import *
from tkinter import messagebox
class NLPApp:
    
    def __init__(self):
        
        self.dbo = Database()
        # create object of TK for tkinter GUI
        self.root = Tk()
        
        
        self.apio = API()
        
        # set title of tkinter GUI
        self.root.title('NLPApp')
        
        # to apply custom favicon
        # self.root.iconbitmap()
        
        # set width x height 
        self.root.geometry('350x600')
        
        # to change colour
        #self.root.configure(bg='red')
        
        # call login_gui function
        self.login_gui()
        
        # so tkinter app stays for long time
        self.root.mainloop()
    
    def login_gui(self):
        self.clear()
        
        # to create a heading
        heading = Label(self.root,text='NLPApp')
        
        # to show heading 
        heading.pack(pady=(30,30))
        
        # to edit heading
        heading.configure(font=(34))
        
        label1 = Label(self.root,text='Enter Email')
        
        label1.pack(pady=(10,10))
         
        label1.configure(font=(18))
        
        # to create a box to enter data 
        self.email = Entry(self.root,width=30)
        self.email.pack(pady=(5,10),ipady=4)
        
        
        label2 = Label(self.root,text='Enter Password')
        
        label2.pack(pady=(10,10))
         
        label2.configure(font=(18))
        
        # to create a box to enter data 
        self.pasword = Entry(self.root,width=30,show='*')
        self.pasword.pack(pady=(5,10),ipady=4)
        
        
        # button class
        login_button = Button(self.root,text='Login',width=20,height=2,command=self.perform_login)
        login_button.pack(pady=(10,10))
        
        # not a member heading
        label3 = Label(self.root,text='Not a member register now')
        label3.pack(pady=(100,10))
        label3.configure(font=(24))
        
        # register button
        register_button = Button(self.root,text='Register',width=15,height=2,command=self.register_gui)
        register_button.pack(pady=(30,10))
        
    
    def perform_login(self):
        email = self.email.get()
        password = self.pasword.get()
        
        response = self.dbo.check_data(email,password)
        if response:
            messagebox.showinfo('Success','You have successfully logged in')
            self.home_gui()
        else:
            messagebox.showerror('Error','Wrong Email/Password')
        
    
    def home_gui(self):
        for i in self.root.pack_slaves():
            i.destroy()
            
        label1 = Label(self.root,text='NLPApp')
        label1.pack(pady=(30,30))
        
        ner_button = Button(self.root,text='Named Entity Recognition',width=20,height=4,command=self.ner_gui)
        ner_button.pack(pady=(40,40))
        
        sentiment_button = Button(self.root,text='Sentiment Analysis',width=20,height=4,command=self.sentiment_gui)
        sentiment_button.pack(pady=(40,40))
        
        summarize_button = Button(self.root,text='Text Summarizaton',width=20,height=4,command=self.summarize_gui)
        summarize_button.pack(pady=(40,10))
         
        logout_button = Button(self.root,text='Logout',width=10,height=2,command=self.login_gui)
        logout_button.pack(pady=(20,30))


    def summarize_gui(self):
        for i in self.root.pack_slaves():
            i.destroy()
        
        label1 = Label(self.root,text='NLPApp',width=20,height=2)
        label1.pack(pady=(30,10))
        label1.configure(font=(30))
        
        label2 = Label(self.root,text='Text Summarization',width=20,height=2)
        label2.pack(pady=(10,20))
        label2.configure(font=(20))


        label3 = Label(self.root,text='Enter Text')
        label3.pack(pady=(30,10))
        label3.configure(font=(10))
        
        self.summarize_input  = Entry(self.root,width=35)
        self.summarize_input.pack(ipady=40,ipadx=40)         

        summarize_button = Button(self.root,text='Summarize',command=self.do_summarize)
        summarize_button.pack(pady=(30,30))

        self.sumarize_result = Label(self.root,text='')
        self.sumarize_result.pack(pady=(30,10))
        self.sumarize_result.configure(font=("Arial", 8))

        
        
        goback_button = Button(self.root,text='Go back',command=self.home_gui)
        goback_button.pack(pady=(30,30))
    
    
    def do_summarize(self):
        text = self.summarize_input.get()
        result = self.apio.text_summarization(text)
        s = result['summary_text'].split('.')
        a = ''.join([a for a in s])
        d = a.split(',')
        # print(d)
        ans=''
        for i in d:
            ans+=str(i)+'\n'
        self.sumarize_result['text'] = ans
    
    
    
    def ner_gui(self):
        for i in self.root.pack_slaves():
            i.destroy()
        
        label1 = Label(self.root,text='NLPApp',width=20,height=2)
        label1.pack(pady=(30,10))
        label1.configure(font=(30))
        
        label2 = Label(self.root,text='Named Entity Recognition',width=20,height=2)
        label2.pack(pady=(10,20))
        label2.configure(font=(20))

        label4 = Label(self.root,text='Entity to Search')
        label4.pack(pady=(30,10))
        label4.configure(font=(10))
        
        self.ner_entity_search  = Entry(self.root,width=35)
        self.ner_entity_search.pack(ipady=2)


        label3 = Label(self.root,text='Enter Text')
        label3.pack(pady=(30,10))
        label3.configure(font=(10))
        
        self.ner_input  = Entry(self.root,width=35)
        self.ner_input.pack(ipady=2)         

        ner_button = Button(self.root,text='Perform NER',command=self.do_NER)
        ner_button.pack(pady=(30,30))

        self.sentiment_result = Label(self.root,text='')
        self.sentiment_result.pack(pady=(30,10))
        
        
        goback_button = Button(self.root,text='Go back',command=self.home_gui)
        goback_button.pack(pady=(30,30))
        
    
    def do_NER(self):
        text = self.ner_input.get()
        searched_entity = self.ner_entity_search.get()
        ans = ''
        result = self.apio.ner_analysis(text,searched_entity)
        for i in result['entities']:
            ans+= 'start: '+ str(i['start'])+' end: '+str(i['end'])+' Text found: '+str(i['text'])+'\n'
        self.sentiment_result['text'] = ans 

    def sentiment_gui(self):
        for i in self.root.pack_slaves():
            i.destroy()
        
        label1 = Label(self.root,text='NLPApp',width=20,height=2)
        label1.pack(pady=(30,10))
        label1.configure(font=(30))
        
        label2 = Label(self.root,text='Sentiment Analysis',width=20,height=2)
        label2.pack(pady=(10,20))
        label2.configure(font=(20))

        label3 = Label(self.root,text='Enter Text')
        label3.pack(pady=(30,10))
        label3.configure(font=(10))
        
        self.sentiment_input  = Entry(self.root,width=35)
        self.sentiment_input.pack(ipady=2)         

        sentiment_button = Button(self.root,text='Analyze Sentiment',command=self.do_sentiment_analysis)
        sentiment_button.pack(pady=(30,30))

        self.sentiment_result = Label(self.root,text='')
        self.sentiment_result.pack(pady=(30,10))
        
        
        goback_button = Button(self.root,text='Go back',command=self.home_gui)
        goback_button.pack(pady=(30,30))
        
        
    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)
        ans = ''
        for j in result['scored_labels']:
            ans += str(j['label'])+'->'+str(j['score'])+'\n'
        self.sentiment_result['text'] = ans
        
    
    
        
    def register_gui(self):
        #clear the eisting GUI 
        self.clear()

        label1 = Label(self.root,text='NLPApp',width=20,height=2)
        label1.pack(pady=(30,10))
        label1.configure(font=(30))
        
        label2 = Label(self.root,text="Enter Name",width=20,height=2)
        label2.pack(pady=(30,10))
        label2.configure(font=(30))
        
        self.name = Entry(self.root,width=20)
        self.name.pack(ipady=2)
        
        label3 = Label(self.root,text="Enter Email",width=20,height=2)
        label3.pack(pady=(30,10))
        label3.configure(font=(30))

        self.email = Entry(self.root,width=20)
        self.email.pack(ipady=2) 
        
        label4 = Label(self.root,text="Enter Password",width=20,height=2)
        label4.pack(pady=(30,10))
        label4.configure(font=(30))
        
        self.pasword = Entry(self.root,show='*',width=20)
        self.pasword.pack(ipady=2,pady=(0,20))
        
        register_button = Button(self.root,text='Register',command=self.perform_registration)
        register_button.pack()
        
        label5 = Label(self.root,text='Already a member?',width=20,height=2)
        label5.pack(pady=(40,5))
        label5.configure(font=(30))
        
        login_button = Button(self.root,text='Login',command=self.login_gui)
        login_button.pack() 
        
               
    def perform_registration(self):
        name = self.name.get()
        email = self.email.get()
        password = self.pasword.get()
        
        response = self.dbo.add_data(name,email,password)
        if response:
            messagebox.showinfo('Success','Registration Successfully done')
        else:
            messagebox.showerror('Error','Email Already exist')
               
               
               
               
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    
nlp = NLPApp()
        