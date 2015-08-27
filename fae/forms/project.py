__author__ = 'fohnwind'

from flask_wtf import Form
from wtforms import (StringField, PasswordField, BooleanField, HiddenField,
                     SubmitField, TextAreaField, SelectField, FileField)
from wtforms.validators import (DataRequired, InputRequired, Email, EqualTo,
                                regexp, ValidationError)
from fae.models.user import User
from flask_babelex import lazy_gettext as _
from fae.models.project import Project


class CreateProjectForm(Form):
    pname = StringField(_("Project name"), validators=[
        DataRequired(message=_("A project name is required."))])

    ptype = SelectField(_("Choose a project type"), choices=[('fwd-ng','nginx'),('fwd-php','nginx-php'),
                                                ('mysql','mysql'),('redis','redis')])
    intro = TextAreaField(_("Project introduction"))
    submit = SubmitField("Create!")
    path = FileField(_("file path"))

    def save(self, user):
        uid = user.get_id()
        #url = "http://" + self.pname.data + ".fae.com"
        project = Project(pname=self.pname.data, owner=uid, intro=self.intro.data,ptype=self.ptype.data)
        return project.save()


class UpdateProjectForm(Form):
    pass
