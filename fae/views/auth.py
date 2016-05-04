__author__ = 'fohnwind'

from flask import ( Blueprint,render_template, redirect, url_for ,request, 
                   flash, session )
import requests

auth = Blueprint("auth", __name__)


@auth.route("/login",methods=["POST"])
def login():
    username = request.form.get("username")
    session['id'] = username
    return redirect(url_for("user.index"))

@auth.route("/sso",methods=["POST"])
def sso():
    """sso login part"""
    token = request.form.get("token") 

    verify_url = "http://sso.fae.com/api/verify?token={}".format(token)
    apiResp = requests.get(verify_url).json()

    if apiResp['ret']:
        session.permanent = True
        session['id'] = apiResp['userid']
        return redirect(url_for('user.index'))


@auth.route("/logout", methods=["GET","POST"])
def logout():
    del session['id']
    return redirect(url_for("homepage.index"))


