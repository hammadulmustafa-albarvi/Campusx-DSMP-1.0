from flask import Flask,render_template,request,session,redirect
from database import *
from api import *


nlpapp = Flask(__name__)
database = Database()
api = Api()
@nlpapp.route('/')
def home_page():
    return render_template('homepage.html')


@nlpapp.route('/login_backend',methods=['post'])
def login_backend():
    email = request.form.get('email')
    password = request.form.get('password')
    result = database.login_backend(email,password)
    if result == 1:
        session
        return render_template("dashboard.html")
    else:
        return render_template("homepage.html",error="Invalid Email/Password")
    
    
@nlpapp.route('/dashboard')
def dashboard():
    if session:
        return render_template('dashboard.html')
    else:
        return redirect('/')

@nlpapp.route('/ner_backend',methods=['post'])
def ner_backend():
    entity = request.form.get("search")
    text = request.form.get("text")
    result = api.ner(text,entity)
    ans = ""
    for i in result['entities']:
        ans+="Start: " + str(i['start']) + " End: " + str(i['end']) + " Word: " + str(i['text']) + "\n"
    return render_template('dashboard.html',ans=ans)
    
@nlpapp.route('/register')
def register_page():
    return render_template('register.html')


@nlpapp.route('/register_backend',methods=['post'])
def register_backend():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    result = database.register_data(name,email,password)
    if result == 1:
        return render_template('homepage.html',info='Successfully Registered')
    else:
        return render_template('register.html',info='Email already Registered')


nlpapp.run(debug=True)
