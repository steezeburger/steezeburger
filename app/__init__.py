__author__ = 'js'

from flask import Flask, url_for

# creates instance of Flask class named 'app'
app = Flask(__name__)
from app import views
