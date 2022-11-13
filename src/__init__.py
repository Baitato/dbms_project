from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db_details = {
    'username': 'root',
    'password': 'prasham28dec',
    'host': 'localhost',
    'database': 'blog_database',
}

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://{username}:{password}@{server}/{db}'.format(
    username=db_details['username'], password=db_details['password'], server=db_details['host'], db=db_details['database'])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SECRET_KEY"]=os.environ.get('SECRET_KEY')
app.config["DEBUG"] = True

# Flask features are inaccessible without a secret key
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)

from src import routes