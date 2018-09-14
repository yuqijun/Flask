from App import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100), default="summer", unique=False)
    telephone = db.Column(db.BigInteger,  nullable=False)
    password = db.Column(db.Integer, nullable=False)                                                           #d


class Question(db.Model):
    __tablename__ = 'question'
    message_id =db.Column(db.Integer,primary_key=True,unique=True,nullable=False)
    caption =db.Column(db.String(60),unique=True)
    content= db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    newer_id =db.Column(db.Integer,db.ForeignKey('user.id'))

    author = db.relationship('User',backref='questions')


class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.Integer,db.ForeignKey('question.message_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    question = db.relationship('Question',backref='answere')
    user = db.relationship('User', backref='answere')