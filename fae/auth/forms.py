__author__ = 'fohnwind'


from wtforms import (StringField, PasswordField, BooleanField, HiddenField,
                     SubmitField)

from wtforms.validators import (DataRequired, InputRequired, Email, EqualTo,
                                regexp, ValidationError)


class LoginForm(Form):
    login = StringField(_("Username or E-Mail Address"), validators=[
        DataRequired(message=_("A Username or E-Mail Address is required."))]
    )

    password = PasswordField(_("Password"), validators=[
        DataRequired(message=_("A Password is required."))])

    remember_me = BooleanField(_("Remember Me"), default=False)

    submit = SubmitField(_("Login"))

