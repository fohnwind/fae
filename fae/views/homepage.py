__author__ = 'fohnwind'

from flask import Blueprint,render_template, send_from_directory

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

@homepage.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory('/home/fohnwind/fae/html/uploads',filename)

