from . import ModelMixin
from . import db
import time
from . import timestamp


class Reply(db.Model, ModelMixin):
    __tablename__ = 'replys'
    id = db.Column(db.Integer, primary_key=True)
    # content = db.Column(db.String(1000))
    content = db.Column(db.String())
    created_time = db.Column(db.Integer)
    # 一对一关系
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, form):
        self.content = form.get('content', '')
        self.created_time = int(time.time())
        self.comment_id = int(form.get('CommentId', 0))

    def json(self):
        d = dict(
            content=self.content,
            created_time=self.created_time,
            username=self.user.username,
            avatar=self.user.avatar,
        )
        return d

    def valid(self):
        return len(self.content) > 0

    def error_message(self):
        if len(self.content) == 0:
            return '内容不能为空'