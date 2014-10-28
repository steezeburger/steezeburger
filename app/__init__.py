__author__ = 'js'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

# creates Flask object and config
app = Flask(__name__)
app.config.from_object('config')
# database object
db = SQLAlchemy(app)
# login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app.models import User

# user loader callback
@login_manager.user_loader
def load_user(id):
    # ids in Flask-Login are Unicode. Convert to int before query
    return User.query.get(int(id))

from app import views, models
