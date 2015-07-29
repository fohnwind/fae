__author__ = 'fohnwind'

from flask import Blueprint,render_template

auth = Blueprint("auth", __name__)

@auth.route("/")
def auth_index():
    return "auth index"