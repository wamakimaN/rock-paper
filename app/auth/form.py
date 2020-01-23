from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

# form for registration










# form for login
class LoginForm(FlaskForm):
    username = StringField('Email',validators = [Required(),Email()])
    password = PasswordField('Password',validators = [Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')




