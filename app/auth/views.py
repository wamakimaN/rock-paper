from flask import render_template,redirect,url_for,flash,request
from flask_wtf import FlaskForm
from ..models import User
from flask_login import login_user,logout_user,login_required
from .form import RegistrationForm
from . import auth
from .. import db

# signup route
@auth.route('/signup',methods=['GET','POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
    return render_template('auth/signup.html',form=form)    












# login route






