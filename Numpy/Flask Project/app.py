from flask import *
import json
from database import *
from api import * 


app = Flask(__name__)

database = DataBase()
api = Api()

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')



@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get ('Name')
    email = request.form.get('Email')
    password = request.form.get('Password')
    result = database.register_backend(name,email,password)
    if result == 1:
        return render_template('login.html',message="You have been successfully registered Kindly login")
    else:
        return render_template('register.html',message="Email Already exist kindly use new email or Log in")
    
    


@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get('email')
    password = request.form.get('password')
    result = database.login_backend(email,password)
    if result == 1:
        return redirect('/profile')
    else:
        return "No welcome"

 

@app.route('/profile')
def profile():
    return render_template('/profile.html')
    

@app.route('/ner')
def ner():
    return render_template('ner.html')


@app.route('/perform_ner',methods=['post'])
def perform_ner():
    search = request.form.get('search')
    text = request.form.get('text')
    result = api.ner(text,search)
    text = ''
    for data in result['entities']:
        text+=' ' + str(data['start']) + " " + str(data['end']) + " " + str(data['text']) + "\n"
    return render_template('ner.html',text=text)
    


app.run(debug=True)



