from . import db
from datetime import datetime 
from flask_login import UserMixin
from . import login_manager

class User(UserMixin,db.MOdel):
    __tablename__="users"
    id =db.Column(db.Integer,Primary_key = True)
    username = db.Column(db.Integer,Primary_key = True)
    password = db.Column(db.Integer,Primary_key = True)
    score = db.Column(db.Integer,Primary_key = True)