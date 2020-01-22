from app import db
from datetime import datetime 
from flask_login import UserMixin
from . import login_manager

class User(UserMixin,db.Model):
    __tablename__="users"
    id =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60),unique = True,nullable = False)
    password = db.Column(db.String(200),nullable = False)
    score = db.Column(db.Integer)

    def __repr__(self):
        return f"User('{self.username}','{self.score}')"