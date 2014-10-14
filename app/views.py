__author__ = 'js'

from app import app
from flask import render_template, url_for, g
from random import choice
from os import listdir

# picks a random picture to display as banner
# can call {{ g.banner }} in template
@app.before_request
def random_banner():
    banner_choice = choice(listdir('app/static/images/banners'))
    g.banner = url_for('static', filename='images/banners/' + banner_choice)

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/glitch/exhibition/')
def glitch_exhibition():
    return render_template('glitch-exhibition.html')

@app.route('/glitch/tutorials/')
def glitch_tutorials():
    return render_template('glitch-tutorials.html')

@app.route('/projects/glitchy/')
def projects_glitchy():
    return render_template('projects-glitchy.html')