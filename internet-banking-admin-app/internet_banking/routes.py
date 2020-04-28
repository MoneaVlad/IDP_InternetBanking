from flask import render_template, url_for, flash, redirect, request, jsonify
from internet_banking import app, db
from internet_banking.models import User, Transaction, UserSchema, TransactionSchema

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/users")
def users():
	users = User.query.all()
	return render_template('users.html', title='Users', users=users)

@app.route("/transactions")
def transactions():
	transactions = Transaction.query.all()

	return render_template('transactions.html', title='Transactions', transactions=transactions)
