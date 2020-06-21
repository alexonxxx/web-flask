from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	"""docstring for RegistrationForm"""
	def __init__(self):
		username=StringField("Username",validators=[DataRequired(),Length(min=2,max=20)])
		email=StringField("Email",validators=[DataRequired(),Email()])
		password=PasswordField("Password",validators=[DataRequired()])
		confirm=PasswordField("Confirm password",validators=[DataRequired(),EqualTo('password')])
		submit=SubmitField("Sign up")
 		FlaskForm.__init__(self)

class LoginForm(FlaskForm):
	"""docstring for RegistrationForm"""
	def __init__(self):
		email=StringField("Email",validators=[DataRequired(),Email()])
		password=PasswordField("Password",validators=[DataRequired()])
		remember=BooleanField("Remember me")
		submit=SubmitField("Sign in")
 		FlaskForm.__init__(self)