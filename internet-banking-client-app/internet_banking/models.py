from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from internet_banking import db, ma, login_manager, app
from flask_login import UserMixin
import rstr

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

def random_iban():
	rand = rstr.xeger(r'OB\d\d\d\d\d\d\d\d\d\d')
	
	# # check if exists in database.
	# from sqlalchemy.orm import sessionmaker
	# db_session_maker = sessionmaker(bind=db)
	# db_session = db_session_maker()
	# while db_session.query(User).filter(iban == rand).limit(1).first() is not None:
	# 	rand = rstr.xeger(r'OB\d\d\d\d\d\d\d\d\d\d')

	return rand

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	iban = db.Column(db.String(10), unique=True, nullable=False, default=random_iban)
	first_name = db.Column(db.String(20), nullable=False)
	last_name = db.Column(db.String(20), nullable=False)
	ci_series = db.Column(db.String(2), nullable=False)
	ci_number = db.Column(db.Integer, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	balance = db.Column(db.Float, nullable=False, default=500.0)
	transactions = db.relationship('Transaction', backref='author', lazy=True)

	def get_login_token(self, expires_sec=1800):
		s = Serializer(app.config['SECRET_KEY'], expires_sec)
		return s.dumps({'user_id': self.id}).decode('utf-8')

	@staticmethod
	def verify_login_token(token):
		s = Serializer(app.config['SECRET_KEY'])
		try:
			user_id = s.loads(token)['user_id']
		except:
			return None
		return User.query.get(user_id)

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