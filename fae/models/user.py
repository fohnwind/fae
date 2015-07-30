__author__ = 'fohnwind'

from fae.extensions import db


class User(db.Model):

    __tablename__ = 'user'

    id = db.Colunm(db.Integer, primary_key=True)
    username = db.Colunm(db.String(200), unique=True, nullable=False)

    pass