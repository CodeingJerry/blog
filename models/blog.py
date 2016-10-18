from . import ModelMixin
from . import db
import time
from . import timestamp


# relationtable = db.Table('relationtable',
#                          db.Column('blog_id', db.Integer, db.ForeignKey('blogs.id')),
#                          db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
#                          )

class Blog(db.Model, ModelMixin):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    # title = db.Column(db.String(100))
    # content = db.Column(db.String(8000))
    title = db.Column(db.String())
    picture = db.Column(db.String())
    abstract = db.Column(db.String())
    content = db.Column(db.String())
    upcount = db.Column(db.Integer)
    downcount = db.Column(db.Integer)
    created_time = db.Column(db.Integer)
    updated_time = db.Column(db.Integer)
    # has relationship with comments 一对多关系(Comment是类名)
    comments = db.relationship('Comment', backref="blog")

    # 多对多关系
    # tags = db.relationship('Tag', secondary=relationtable, backref="blogs")

    # 一对一的关系用外键（users tags是表名）
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))

    def __init__(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.upcount = int(form.get('upcount', 0))
        self.downcount = int(form.get('downcount', 0))
        self.abstract = form.get('abstract', '')
        self.picture = r'http://res.myform.com/mmexport1446764829446.jpg'
        self.created_time = int(time.time())
        self.updated_time = int(time.time())

    def update(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.tag_id = form.get('tag_id', '')
        self.updated_time = int(time.time())
        self.save()

    def json(self):
        d = dict(
            title=self.title,
            content=self.content,
            upcount=self.upcount,
            downcount=self.downcount,
            created_time=self.created_time,
            updated_time=self.updated_time,
        )
        return d