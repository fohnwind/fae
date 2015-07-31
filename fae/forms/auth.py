__author__ = 'fohnwind'


from flask_wtf import Form , RecaptchaField
from wtforms import (StringField, PasswordField, BooleanField, HiddenField,
                     SubmitField)
from wtforms.validators import (DataRequired, InputRequired, Email, EqualTo,
                                regexp, ValidationError)
from fae.models.user import User

USERNAME_RE = r'^[\w.+-]+$'
is_username = regexp(USERNAME_RE,
                     message="You can only use letters, numbers or dashes.")

class LoginForm(Form):
    login = StringField("Username", validators=[
        DataRequired(message="a username is required.")
    ])

    password = PasswordField("password", validators=[
        DataRequired(message="a password is required.")
    ])

    remember_me = BooleanField("Rememberme", default=False)

    submit = SubmitField("Login")


class RegisterForm(Form):
    pass