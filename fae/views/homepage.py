__author__ = 'fohnwind'

from flask import Blueprint,render_template

homepage = Blueprint("homepage", __name__)

@homepage.route("/")
@homepage.route("/index")
@homepage.route("/homepage")
def index():
    return render_template("homepage/index.html")


@homepage.route("/about")
def about():
    return render_template("homepage/about.html")


@homepage.route("/guide")
def guide():
    return render_template("homepage/guide.html")