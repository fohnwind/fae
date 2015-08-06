#__author__ = 'fohnwind'


from flask_wtf import Form, RecaptchaField
from wtforms import (StringField, PasswordField, BooleanField, HiddenField,
                     SubmitField, TextField)
from wtforms.validators import (DataRequired, InputRequired, Email, EqualTo,
                                regexp, ValidationError)
from fae.models.user import User
from flask_babelex import lazy_gettext as _
USERNAME_RE = r'^[\w.+-]+$'
is_username = regexp(USERNAME_RE,
                     message="You can only use letters, numbers or dashes.")


class LoginForm(Form):
    username = StringField(_("Username"))

    password = StringField(_("Password"))

    remember_me = BooleanField(_("Remember me"), default=False)

    submit = SubmitField(_("Sign in"))


class RegisterForm(Form):
    username = StringField("Username",validators=[
        DataRequired(message="a username is required.")
    ])

    password = PasswordField("Password", validators=[
        DataRequired(message="a password is required.")
    ])

    confirm_password= PasswordField("Confirm password.")

    submit = SubmitField("Register")

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError("Username already exsits.")

    def save(self):
        user = User(username=self.username.data,
                    password=self.password.data,
                    project_count=0,
                    user_level=0)

        return user.save()

