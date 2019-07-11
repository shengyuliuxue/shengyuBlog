from blog.extensions import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime)
    category
    comments


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.string(20), nullable=False)
    post

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reply = db.Column(db.String(100))  #如果超出？
    author
    comment 






