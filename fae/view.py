__author__ = 'fohnwind'


from flask import render_template
from fae import app

@app.route("/")
@app.route("/index")

def home():
    return "homepage"

