__author__ = 'fohnwind'

from fae.extensions import db


class Project(db.Model):
    __tablename__ = 'project'

    pid = db.Column(db.Integer(), primary_key=True)

    pass