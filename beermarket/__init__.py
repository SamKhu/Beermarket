from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///beermarket1.db'
app.config['SECRET_KEY']='b5c32fe658156cdbd3abefc3'
db = SQLAlchemy(app)


from beermarket import routes

