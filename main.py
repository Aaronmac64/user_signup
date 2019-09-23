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
    error = "There was an error"

    pushToResult = True

    if username == "":
        pushToResult = False
        error = "Username field was empty!"

    if password == "":
        pushToResult = False
        error = "Password field was empty!"

    if verify_password == "":
        pushToResult = False
        error = "Verify Password field was empty!"

    if " " in password:
        pushToResult = False
        error = "Password had unsupported characters"

    if len(password) < 3:
        pushToResult = False
        error = "Password is too short"

    if len(password) > 20:
        pushToResult = False
        error = "Password is too long"

    if email != "":
        if any(["@" in email]):
            error = ""
        else:
            pushToResult = False
            error = "Email did not contain @ sign"
        if any([" " in email]):
            pushToResult = False
            error = "Email cannot contain any spaces"
        if any(["." in email]):
            error = ""
        else:
            pushToResult = False
            error = "Email did not contain any periods"


    if verify_password != password:
        pushToResult = False
        error = "Verify Password did not match Password!"

    if pushToResult:
        return render_template('result_form.html',username=username)
    else:
        return redirect("/?error=" + error)

app.run()