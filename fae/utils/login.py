# -*- coding:utf-8 -*-

from flask import session, redirect, url_for
from functools import wraps

def login_r(fn):

    @wraps(fn)
    def check_session(*args, **kargs):
        if not session.get("id"):
            return redirect(url_for('homepage.index'))
        return fn(*args, **kargs)
    return check_session
