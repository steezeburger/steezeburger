__author__ = 'js'

from app import app
from flask import redirect, render_template, request, url_for, g, send_from_directory
from random import choice
import os
from werkzeug.utils import secure_filename
import glitchy
from PIL import Image

# allowed file extensions for jpg glitcher upload form
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS_TBG']

# picks a random picture to display as banner
# can call {{ g.banner }} in jinja template
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
            print 'extension allowed'
            filename = secure_filename(file.filename)
            print filename + ' secured'
            file.save(os.path.join(app.config['UPLOAD_FOLDER_GLITCHY'], filename))
            print filename + ' saved'
            image_location = app.config['BASE_DIR'] + '/app/static/images/glitched/' + filename
            filename = glitchy.glitch(image_location)
            #Image.open(image_location).save(image_location)
            print filename + ' glitched'

            return redirect(url_for('glitched', filename=filename))

    return render_template('projects-glitchy.html')

@app.route('/glitched/<filename>')
def glitched(filename):
    print filename
    return send_from_directory(app.config['UPLOAD_FOLDER_GLITCHY'],
                               filename, mimetype='image/jpeg')
