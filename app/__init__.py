from flask import Flask, render_template
app = Flask(__name__)

from flask_bootstrap import Bootstrap

bootstrap = Bootstrap(app)


from app import routes
