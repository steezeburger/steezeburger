__author__ = 'js'

from app import app

from flask import (redirect, render_template, request, url_for,
                   g, send_from_directory, Markup, session, abort,
                   flash)

from flask.ext.login import (login_user, logout_user, current_user,
                             login_required)

from app.models import User

from random import choice
import os
from os.path import isfile, join
from werkzeug.utils import secure_filename
from PIL import Image
import markdown
import glitchy


# allowed file extensions for jpg glitcher upload form
def allowed_files_glitch(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS_TBG']


# allowed file extentions for tutorial upload form
def allowed_files_tutorials(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS_TUTORIALS']


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
    return render_template('glitch-exhibition.html', title='.glitch')


@app.route('/glitch/tutorials/')
def glitch_tutorials():
    return render_template('glitch-tutorials.html', title='.glitch-tutorials')


@app.route('/projects/glitchy/', methods=['GET', 'POST'])
def projects_glitchy():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_files_glitch(file.filename):
            print 'extension allowed'
            filename = secure_filename(file.filename)
            print filename + ' secured'
            file.save(os.path.join(app.config['UPLOAD_FOLDER_GLITCHY'], filename))
            print filename + ' saved'
            image_location = app.config['BASE_DIR'] + '/app/static/images/glitched/' + filename
            filename = glitchy.glitch(image_location)
            Image.open(image_location).save(image_location)
            print filename + ' glitched'

            return redirect(url_for('glitched', filename=filename))

    return render_template('projects-glitchy.html', title='.glitchy')


@app.route('/glitched/<filename>/')
def glitched(filename):
    print filename
    return send_from_directory(app.config['UPLOAD_FOLDER_GLITCHY'],
                               filename, mimetype='image/jpeg')


@app.before_request
def before_request():
    g.user = current_user


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', title='.login')
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    print user
    if user is not None and user.verify_password(password):
        login_user(user)
        flash('login succesful')
        return redirect(url_for('tutorials_upload'))
    flash('username or password is invalid', 'error')
    return redirect(url_for('login'))


@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/tutorials/upload/', methods=['GET', 'POST'])
@login_required
def tutorials_upload():
    if request.method == 'POST':
        tutorial_file = request.files['tutorial']
        if tutorial_file and allowed_files_tutorials(tutorial_file.filename):
            print 'extension allowed'
            filename = secure_filename(tutorial_file.filename)
            print filename + ' secured'
            tutorial_file.save(os.path.join(app.config['UPLOAD_FOLDER_TUTORIALS'], filename))
            print filename + ' saved'

            # return redirect(url_for('tutorials'))
            return render_template('tutorials.html', title='.tutorials')

    return render_template('tutorials-upload.html', title='.upload')


@app.route('/tutorials/')
def tutorials():
    tutorials = [f for f in os.listdir(app.config['UPLOAD_FOLDER_TUTORIALS']) if
                 isfile(join(app.config['UPLOAD_FOLDER_TUTORIALS'], f))]
    print tutorials

    contents = []

    for tutorial in tutorials:
        handler = open(app.config['UPLOAD_FOLDER_TUTORIALS'] + '/' + tutorial, 'r')
        content = handler.read()
        handler.close()
        contents.append(Markup(markdown.markdown(content)))

    return render_template('tutorials.html', contents=contents, title='.tutorials')
