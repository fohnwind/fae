from flask import Flask, render_template
from user.views import user

app = Flask(__name__)

app.register_blueprint(user)
#app.register_blueprint(index)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/about/')
def about():
    return render_temppate("about.html")

if __name__ == '__main__':
    app.run()

