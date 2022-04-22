from flask import Flask, render_template, request

app = Flask(__name__)
# export FLASK_APP=main
# run flask run to run local server
@app.route("/")
def hello_world():
    return render_template('index.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()
