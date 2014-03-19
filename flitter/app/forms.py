from flask.ext.wtf import Form, PasswordField
from wtforms import TextField, BooleanField, SubmitField
from wtforms.validators import Required, Length
from models import User, Post
from flask import g

class LoginForm(Form):
    username = TextField('Username or Email:', validators =[Required()])
    password = PasswordField('Password:', validators =[Required()])
    submit = SubmitField('Login')
    remember_me = BooleanField('remember_me', default = False)

class RegisterForm(Form):
	fullname = TextField('Full Name:', validators =[Required()])
	newusername = TextField('Username or Email:', validators =[Required()])
	password = PasswordField('Password:', validators=[Required()])
	submit = SubmitField('Sign Up')

class CreatePostForm(Form): #limit to 200 characters can be inserted, this done on client side as well
	posttext = TextField('Post Content:', validators =[Length(max = 200), Required()])
	submit = SubmitField('New Post')
