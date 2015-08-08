__author__ = 'fohnwind'

from fae.extensions import db


class Container(db.Model):

    __tablename__ = 'container'

    cid = db.Column(db.Integer(), primary_key=True)
    cname = db.Column(db.String(40), nullable=False)
    ip = db.Column(db.String(40), nullable=False, default="172.17.0.0")
    image = db.Column(db.String(40), nullable=False)
    relation = db.Column(db.Integer(), unique=True, nullable=False)

    def create(self, ):
        pass

    def get_ip(self):
        return self.ip

    def set_ip(self, ip):
        self.ip = ip

    def get_relation(self):
        return self.relation

