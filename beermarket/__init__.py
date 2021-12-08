from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///beermarket1.db'
app.config['SECRET_KEY']='b5c32fe658156cdbd3abefc3'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from beermarket import routes

