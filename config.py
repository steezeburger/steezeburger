__author__ = 'js'

import os

# CRSF prevention w/ token
CRSF_ENABLED = True
SECRET_KEY = 'bananapants2014'

# base directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# upload folder for to be glitched images
UPLOAD_FOLDER_GLITCHY = BASE_DIR + '/app/static/images/glitched'

# upload folder for tutorials
UPLOAD_FOLDER_TUTORIALS = BASE_DIR + '/app/static/tutorials'

# allowed extensions for image glitcher uploads.
# currently jpg only
ALLOWED_EXTENSIONS_TBG = set(['jpg', 'jpeg'])

# allowed extensions for tutorial uploads
ALLOWED_EXTENSIONS_TUTORIALS = set(['md'])



