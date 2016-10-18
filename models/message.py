from . import ModelMixin
from . import db
import time
from . import timestamp


class Message(db.Model, ModelMixin):
    __tablename__ = 'manages'
    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(20))
    message = db.Column(db.String())
    status = db.Column(db.Integer)
    created_time = db.Column(db.Integer)

    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self):
        self.status = 0
        self.created_time = int(time.time())

    def json(self):
        d = dict(
            blog_id=self.blog_id,
        )
        return d
