from blog.extensions import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship("Category", back_populates="posts")
    comment = db.relationship('Comment', back_populates='post')


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.string(20), nullable=False)
    posts = db.relationship('Post', back_populates='category')

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reply = db.Column(db.Text)  #如果超出？
    author = db.Column(db.String(30))
    time = db.Column(db.DateTime,default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    replied_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    post = db.relationship('Post', back_populates='comment')
    replies = db.relationship('Comment', back_populates='replied', cascade='all')
    replied = db.relationship('Comment', back_populates='replies')

class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    link = db.Column(db.String(100), nullable=False)






