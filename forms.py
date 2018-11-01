from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
  first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
  last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])
  username = StringField('Username', validators=[DataRequired("Please enter your username"), Length(min=5, message="username must be 5 characters or more")])
  submit = SubmitField('Sign up')

class LoginForm(Form):
  email = StringField('email', validators=[DataRequired("Please enter your username.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
  submit = SubmitField("Sign in")

class tweetform(Form):
  body = TextAreaField("What's on your mind?", validators=[DataRequired("Please enter some text"), Length(min=1, max=300, message="text must be between 1 and 300 characters")])
  timestamp= DateField('data posted', format='%Y-%m-%d')
  author_id = StringField('tweet number')
  submit = SubmitField('Submit')