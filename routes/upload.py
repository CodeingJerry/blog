from routes import *
import os
from flask import Flask, request, redirect, url_for, flash
from werkzeug.utils import secure_filename


main = Blueprint('upload', __name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# @main.route('/', methods=['POST'])
def upload_file():
    # if request.method == 'POST':
    #     # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also submit a empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        print('debug filename0, ', filename)
        file.save(os.path.join(main.config['UPLOAD_FOLDER'], filename))
        return filename
        # return redirect(url_for('uploaded_file',filename=filename))
    # return '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form action="" method=post enctype=multipart/form-data>
    #   <p><input type=file name=file>
    #      <input type=submit value=Upload>
    # </form>
    # '''