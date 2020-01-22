from flask import render_template,redirect,url_for,flash,request
from flask_wtf import FlaskForm
from ..models import User
from flask_login import login_user,logout_user,login_required
from .form import LoginForm,RegistrationForm
from . import auth
from .. import db

# signup route










# login route
@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
  
        flash('Invalid username or Password')

    title = "Login"
    return render_template('auth/login.html',form =form,title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))





