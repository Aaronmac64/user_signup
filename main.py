from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():

    return render_template('submission_form.html',)

@app.route("/result", methods=['POST'])
def resultform():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    return render_template('result_form.html',username=username)

app.run()