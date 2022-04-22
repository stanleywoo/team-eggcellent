import re
from service.ImageUploadService import upload_image
import json
from flask import Flask, render_template, request, flash, redirect, session, send_from_directory, jsonify
import os
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

# export FLASK_APP=main
# run flask run to run local server
@app.route("/")
def hello_world():
    return render_template('type.html')


@app.route("/tutorial")
def tutorial():
    return render_template('tutorial.html')


@app.route("/measurements", methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST' and request.files['image']:
        app.logger.info('./images')
        img = request.files['image']
        img_name = img.filename
        saved_path = os.path.join('./images', img_name)
        app.logger.info("saving {}".format(saved_path))
        img.save(saved_path)
        return jsonify(
            message='we gucci. replace with image'
        )

    if request.method == 'GET':
        return render_template('measurements.html')
