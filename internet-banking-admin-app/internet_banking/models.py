from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from internet_banking import db, ma, app
import rstr

def random_iban():
	rand = rstr.xeger(r'OB\d\d\d\d\d\d\d\d\d\d')

	return rand

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	iban = db.Column(db.String(12), unique=True, nullable=False, default=random_iban)
	first_name = db.Column(db.String(20), nullable=False)
	last_name = db.Column(db.String(20), nullable=False)
	ci_series = db.Column(db.String(2), nullable=False)
	ci_number = db.Column(db.Integer, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	balance = db.Column(db.Float, nullable=False, default=500.0)
	transactions = db.relationship('Transaction', backref='author', lazy=True)

	def __repr__(self):
		return f"User('{self.id}', '{self.first_name}', '{self.last_name}', '{self.email}')"

class Transaction(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	destination = db.Column(db.String(100), nullable=False)
	date_transacted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	details = db.Column(db.Text, nullable=False)
	amount_transacted = db.Column(db.Integer, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Transaction('{self.destination}', '{self.date_transacted}', '{self.user_id}')"

class UserSchema(ma.ModelSchema):
	class Meta:
		model = User

class TransactionSchema(ma.ModelSchema):
	class Meta:
		model = Transaction