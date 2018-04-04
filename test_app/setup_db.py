import flask
from flask import Flask
from flask import render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DB_URI'] = 'sqlite:////comment.db'
db = SQLAlchemy(app)
print(datetime.now())

class comments(db.Model):
    __tablename__ = 'comments'
    comment_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    text = db.Column(db.String)
    date = db.Column(db.DateTime)

    def __init__(self, text):
        self.text = text
        self.date = datetime.now()

class responses(db.Model):
    __tablename__ = 'responses'
    comment_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    text = db.Column(db.String)
    date = db.Column(db.DateTime)

    def __init__(self, text):
        self.text = text
        self.date = datetime.now()


db.create_all()

new_comment = comments(text = 'sadlkfjs')
response_1 = responses(text = 'Oh really? How Insightful')
response_2 = responses(text = 'You don\'t say')
response_3 = responses(text = 'You\'re like a 21st Century Einstein')
response_4 = responses(text = 'Does your Mom tell you your smart? Because you really are.')
response_5 = responses(text = 'Wow. Just wow. Great work.')
db.session.add(new_comment)
db.session.bulk_save_objects([response_1, response_2, response_3, response_4, response_5])
db.session.commit()
