from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User
from wtforms import ValidationError

# form for registration
class RegistrationForm(FlaskForm):
    username = StringField('Enter your username',validators = [DataRequired()])
    password = PasswordField('Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [DataRequired()])
    submit = SubmitField('Sign Up')










# form for login
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators = [DataRequired(),Email()])
    password = PasswordField('Password',validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')




