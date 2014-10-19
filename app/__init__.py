__author__ = 'js'

from flask import Flask

# creates Flask object and config
app = Flask(__name__)
app.config.from_object('config')

from app import views
