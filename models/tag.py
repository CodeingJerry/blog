from . import ModelMixin
from . import db
from . import timestamp


class Tag(db.Model, ModelMixin):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(20))
    name = db.Column(db.String())

    # has relationship with comments 一对多关系(Blog是类名)
    blogs = db.relationship('Blog', backref="tag")

    def __init__(self, form):
        self.name = form.get('name', '')

    def update(self, form):
        self.name = form.get('name', '')
        self.save()
