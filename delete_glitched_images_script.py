__author__ = 'js'

import os
from config import UPLOAD_FOLDER_GLITCHY

for files in os.listdir(UPLOAD_FOLDER_GLITCHY):
    file_path = os.path.join(UPLOAD_FOLDER_GLITCHY, files)
    try:
        os.unlink(file_path)
    except Exception, error:
        print error


