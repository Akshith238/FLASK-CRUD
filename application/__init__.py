from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from application.calculator import Calculator

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/sample'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'laksdjfh'
calculator=Calculator()
db=SQLAlchemy(app)
from application import routes

