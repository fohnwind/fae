__author__ = 'fohnwind'

from fae.extensions import db, docker_manager


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

    def __init__(self, *args, **kwargs):
        super(Container, self).__init__(*args, **kwargs)

    def startup(self):
        container = docker_manager.create_container(image=self.image, name=self.cname, volumes=self.filepath)
        docker_manager.start(container=container.get('Id'))
        exec_item = docker_manager.exec_create(container=self.cname, cmd="/root/getip.sh")
        result = docker_manager.exec_start(exec_id=exec_item.get('Id'))
        return result  # return container IP