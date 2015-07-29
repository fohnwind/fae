__author__ = 'fohnwind'


from wtforms import (StringField, PasswordField, BooleanField, HiddenField,
                     SubmitField)

from wtforms.validators import (DataRequired, InputRequired, Email, EqualTo,
                                regexp, ValidationError)

from fae.user.models import User
class LoginForm(Form):
    login = StringField(_("Username or E-Mail Address"), validators=[
        DataRequired(message=_("A Username or E-Mail Address is required."))]
    )

    password = PasswordField(_("Password"), validators=[
        DataRequired(message=_("A Password is required."))])

    remember_me = BooleanField(_("Remember Me"), default=False)

    submit = SubmitField(_("Login"))


class RegisterForm(Form):
    username = StringField(_("Username"), validators=[
        DataRequired(message=_("A Username is required.")),
        is_username])

    email = StringField(_("E-Mail Address"), validators=[
        DataRequired(message=_("A E-Mail Address is required.")),
        Email(message=_("Invalid E-Mail Address."))])

    password = PasswordField(_('Password'), validators=[
        InputRequired(),
        EqualTo('confirm_password', message=_('Passwords must match.'))])

    confirm_password = PasswordField(_('Confirm Password'))

    accept_tos = BooleanField(_("I accept the Terms of Service"), default=True)

    submit = SubmitField(_("Register"))

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError(_("This Username is already taken."))

    def validate_email(self, field):
        email = User.query.filter_by(email=field.data).first()
        if email:
            raise ValidationError(_("This E-Mail Address is already taken."))

    def save(self):
        user = User(username=self.username.data,
                    email=self.email.data,
                    password=self.password.data,
                    date_joined=datetime.utcnow(),
                    primary_group_id=4)
        return user.save()

