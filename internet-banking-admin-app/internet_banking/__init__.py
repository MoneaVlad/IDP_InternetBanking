from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '54fa52f600be2d552cc4f074ee33ad8c'


DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASS = os.environ["DB_PASS"]
DB_NAME = os.environ["DB_NAME"]
DB_HOST = os.environ["DB_HOST"]

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}:3306/{}'.format(DB_USERNAME, DB_PASS, DB_HOST, DB_NAME)
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

ma = Marshmallow(app)

from internet_banking import routes