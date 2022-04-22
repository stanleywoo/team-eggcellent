from flask import Flask, render_template, request
from service.ImageUploadService import upload_image
app = Flask(__name__)
# export FLASK_APP=main
# run flask run to run local server
@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/uploadImage', methods=['GET'])
def uploadImage():
    if request.method == 'GET':
        return upload_image('url')
