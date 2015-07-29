__author__ = 'fohnwind'
__version__ = '0.0 20150728'
from flask import Flask, render_template
from user.views import user
from extensions import *
app = Flask(__name__)

app.register_blueprint(user)
#app.register_blueprint(index)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_temppate("about.html")

if __name__ == '__main__':
    app.run("0.0.0.0",5555,debug=True)

