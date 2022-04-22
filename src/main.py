import json
from flask import Flask, render_template, request, flash, redirect, session
import os


app = Flask(__name__)

# export FLASK_APP=main
# run flask run to run local server
@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/measurements", methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    filename = file.filename
    file.save(os.path.join('./images', filename))
    return json(filename)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()
