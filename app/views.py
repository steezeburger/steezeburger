__author__ = 'js'

from app import app
from flask import redirect, render_template, request, url_for, g, send_from_directory
from random import choice
import os
from werkzeug import secure_filename
import glitchy

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS_TBG']

# picks a random picture to display as banner
# can call {{ g.banner }} in template
@app.before_request
def random_banner():
    banner_choice = choice(os.listdir(app.config['BASE_DIR'] + '/app/static/images/banners'))
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

@app.route('/projects/glitchy/', methods=['GET', 'POST'])
def projects_glitchy():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            print file.filename
            filename = secure_filename(file.filename)
            print filename + ' secured'
            filename = glitchy.glitch(filename)
            print filename + ' glitched'
            file.save(os.path.join(app.config['UPLOAD_FOLDER_TBG'], filename))
            print filename + ' saved'

            return redirect(url_for('glitched', filename=filename))

    return render_template('projects-glitchy.html')

@app.route('/glitched/<filename>')
def glitched(filename):
    print filename
    return send_from_directory(app.config['UPLOAD_FOLDER_TBG'],
                               filename)
