__auther__ = 'fohnwind'


from extensions import db


class User(db.Model):
    __tablename__ = "users"
    __searchable__ = ['username', 'email']

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    _password = db.Column('password', db.String(120), nullable=False)