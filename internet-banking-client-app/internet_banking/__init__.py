from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '54fa52f600be2d552cc4f074ee33ad8c'


DB_USERNAME = os.environ("DB_USERNAME")
DB_PASS = os.environ("DB_PASS")
DB_NAME = os.environ("DB_NAME")
DB_HOST = os.environ("DB_HOST")
DB_PORT = os.environ("DB_PORT")
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{DB_USERNAME}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
db.create_all()

ma = Marshmallow(app)

bcrypt = Bcrypt(app)        
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'internet.banking69@gmail.com'
app.config['MAIL_PASSWORD'] = 'bgplctzcrt69'
mail = Mail(app)

from internet_banking import routes