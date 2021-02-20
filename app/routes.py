from flask import Flask, render_template
from flask_script import Manager
from flask_moment import Moment

from datetime import datetime




from app import app

from app.models import *

# Home Page
@app.route('/')
def home():
    return render_template('index.html', current_time=datetime.utcnow())
    

# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    pageName = 'login'
    form = loginForm(request.form)
    return render_template('login.html', pageName=pageName, form=form, current_time=datetime.utcnow())
	


#User registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    pageName = 'register'
    form = registrationForm(request.form)
    return render_template('register.html', pageName=pageName, form=form, current_time=datetime.utcnow())


# About App Page
@app.route('/about')
def about():
    return render_template('about.html', current_time=datetime.utcnow())
