__author__ = 'fohnwind'


from flask import Blueprint, render_template

images = Blueprint("images", __name__)

@images.route("/")
def list():
    return render_template("images/list.html")