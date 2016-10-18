from . import ModelMixin
from . import db
import time
from . import timestamp


class Comment(db.Model, ModelMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    # content = db.Column(db.String(1000))
    content = db.Column(db.String())
    created_time = db.Column(db.Integer)
    replys = db.relationship('Reply', backref="comment")
    # 一对一关系
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, form):
        self.content = form.get('content', '')
        self.created_time = int(time.time())
        self.blog_id = int(form.get('blogId', 0))

    def json(self):
        d = dict(
            id=self.id,
            content=self.content,
            created_time=self.created_time,
            blog_id=self.blog_id,
            user_id=self.user_id,
            username=self.user.username,
        )
        return d

    def valid(self):
        return len(self.content) > 0

    def error_message(self):
        if len(self.content) == 0:
            return '评论不能为空'