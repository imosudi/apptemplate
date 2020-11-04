from flask import Flask, render_template
from flask_script import Manager
from flask_moment import Moment

from datetime import datetime




from app import app

@app.route('/')
def home():
    return render_template('index.html', current_time=datetime.utcnow())
