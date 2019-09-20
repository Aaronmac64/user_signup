from flask import Flask, request, redirect
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():

    content = "asdf"
    return content

app.run()