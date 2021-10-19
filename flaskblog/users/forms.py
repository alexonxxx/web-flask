from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User

class RegistrationForm(FlaskForm):
	"""docstring for RegistrationForm"""
	username=StringField("Username",validators=[DataRequired(),Length(min=2,max=20)])
	email=StringField("Email",validators=[DataRequired(),Email()])
	password=PasswordField("Password",validators=[DataRequired()])
	confirm=PasswordField("Confirm password",validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField("Sign up")

	def validate_username(self,username):
		user=User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError("That username is taken. Please choose a different one")

	def validate_email(self,email):
		user=User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError("That email is taken. Please choose a different one")

class LoginForm(FlaskForm):
	"""docstring for LoginForm"""
	
	email=StringField("Email",validators=[DataRequired(),Email()])
	password=PasswordField("Password",validators=[DataRequired()])
	remember=BooleanField("Remember me")
	submit=SubmitField("Sign in")
 	

class UpdateAccountForm(FlaskForm):
	"""docstring for RegistrationForm"""
	username=StringField("Username",validators=[DataRequired(),Length(min=2,max=20)])
	email=StringField("Email",validators=[DataRequired(),Email()])
	picture=FileField("Update Profile Picture", validators=[FileAllowed(["jpg","png","svg"])])
	submit=SubmitField("Update")

	def validate_username(self,username):
		if username.data!=current_user.username:
			user=User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError("That username is taken. Please choos a different one")

	def validate_email(self,email):
		if email.data!=current_user.email:
			email=User.query.filter_by(email=email.data).first()
			if email:
				raise ValidationError("That email is taken. Please choos a different one")

class RequestResetForm(FlaskForm):
	email=StringField("Email",validators=[DataRequired(),Email()])
	submit=SubmitField("Request Password Reset")

	def validate_email(self,email):
		user=User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError("There is no account with that email. You must register first")

class ResetPasswordForm(FlaskForm):
	password=PasswordField("Password",validators=[DataRequired()])
	confirm=PasswordField("Confirm password",validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField("Reset Password")