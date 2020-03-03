from flask import render_template, url_for, flash, redirect, request, jsonify
from internet_banking import app, db, bcrypt, mail
from internet_banking.forms import RegistrationForm, LoginForm, PaymentsForm
from internet_banking.models import User, Transaction, UserSchema, TransactionSchema
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
import datetime

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html', title='About')

@app.route("/register", methods = ['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(first_name=form.first_name.data, last_name=form.last_name.data, 
					ci_series=form.ci_series.data, ci_number=form.ci_number.data,
					email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Contul a fost creat cu succes!', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=None)
			flash('V-ati autentificat cu success!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Datele introduse sunt incorecte! Autentificare esuata!', 'danger')
	return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
	outTransactions = Transaction.query.filter_by(user_id=current_user.id).all()
	inTransactions = Transaction.query.filter_by(destination=current_user.iban).all()
	return render_template('account.html', title='Account', inTransactions=inTransactions, outTransactions = outTransactions)

@app.route("/payments", methods=['GET', 'POST'])
@login_required
def payments():
	form = PaymentsForm()
	if form.validate_on_submit():
		receiver = User.query.filter_by(iban=form.iban.data).first()
		sender = User.query.filter_by(id=current_user.id).first()
		
		if receiver is None:
			flash('IBAN-ul introdus este incorect!', 'warning')
			return redirect(url_for('payments'))
		
		if receiver.first_name == form.first_name.data and receiver.last_name == form.last_name.data:
			if sender.balance < form.sum.data:
				flash('Soldul curent nu este suficient pentru efectuarea tranzacţiei!', 'warning')
				return redirect(url_for('payments'))
			
			transaction = Transaction(destination=receiver.iban, date_transacted=datetime.datetime.now(),
										details=form.details.data, amount_transacted=form.sum.data, user_id=sender.id)
			
			sender.balance -= form.sum.data
			receiver.balance += form.sum.data
			
			db.session.add(transaction)
			db.session.commit()

			flash('Transferul a fost realizat!', 'success')
			return redirect(url_for('account'))
		
		else:
			flash('Datele destinatarului sunt incorecte!', 'warning')
			return redirect(url_for('payments'))
	
	return render_template('payments.html', title='Payments', form=form)


