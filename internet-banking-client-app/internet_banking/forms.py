from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from internet_banking.models import User, Transaction


class RegistrationForm(FlaskForm):
	first_name = StringField('Prenume', validators=[DataRequired(), Length(min=2, max=20)])
	last_name = StringField('Nume', validators=[DataRequired(), Length(min=2, max=20)])
	ci_series = StringField('Serie CI', validators = [DataRequired(), Length(min=2, max=2)])
	ci_number = StringField('Numar CI',	validators = [DataRequired(), Length(min=6, max=6)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Parola', validators = [DataRequired()])
	confirm_password = PasswordField('Confirmarea Parolei',	validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField('Creeaza cont')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
	email = StringField('Email',
						validators=[DataRequired(), Email()])
	password = PasswordField('Parola',
						validators = [DataRequired()])
	submit = SubmitField('Login')

class PaymentsForm(FlaskForm):
	first_name = StringField('Prenume destinatar', validators=[DataRequired(), Length(min=2, max=20)])
	last_name = StringField('Nume destinatar', validators=[DataRequired(), Length(min=2, max=20)])	
	iban = StringField('IBAN destinatar', validators=[DataRequired()])
	sum = FloatField('Valoare transfer', validators=[DataRequired()])
	details = StringField('Detalii transfer', validators=[DataRequired()])
	submit = SubmitField('Transferă')


