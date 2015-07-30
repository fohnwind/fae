__author__ = 'fohnwind'


from flask_wtf import Form , RecaptchaField
from wtforms import (StringField, PasswordField, BooleanField, HiddenField,
                     SubmitField)
from wtforms.validators import (DataRequired, InputRequired, Email, EqualTo,
                                regexp, ValidationError)
from fae.models.user import User

USERNAME_RE = r'^[\w.+-]+$'
is_username = regexp(USERNAME_RE,
                     message=_("You can only use letters, numbers or dashes."))

class LoginForm(Form):
    login = StringField(_("Username"), validators=[
        DataRequired(message=_("a username is required."))
    ])

    password = PasswordField(_("password"), validators=[
        DataRequired(message=_("a password is required."))
    ])

    remember_me = BooleanField(_("Rememberme"), default=False)

    submit = SubmitField(_("Login"))

class RegisterForm(Form):
    pass