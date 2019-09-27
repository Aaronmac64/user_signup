from flask import Flask, request, redirect, render_template, url_for
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

usernameError = ""
passwordError = ""
passwordVerifyError = ""
emailError = ""

@app.route("/")
def index():

    usernameError = " "
    passwordError = " "
    passwordVerifyError = " "
    emailError = " "

    usernameField = ""
    emailField = ""

    usernameField = request.form.get('username')
    #if not usernameField:
    #    usernameField = ""

    emailField = request.form.get('email')    
    #if not emailField:
    #    emailField = ""

    usernameError = request.args.get("usernameError")
    if not usernameError:
        usernameError = " "

    passwordError = request.args.get("passwordError")
    if not passwordError:
        passwordError = " "

    passwordVerifyError = request.args.get("passwordVerifyError")
    if not passwordVerifyError:
        passwordVerifyError = " "

    emailError = request.args.get("emailError")
    if not emailError:
        emailError = " "

    return render_template('submission_form.html', usernameError=usernameError, passwordError=passwordError, passwordVerifyError=passwordVerifyError, emailError=emailError, emailField=emailField, usernameField=usernameField)

@app.route("/result", methods=['POST', 'GET'])
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
        return redirect("/?usernameError=" + error)

    if password == "":
        pushToResult = False
        error = "Password field was empty!"
        return redirect("/?passwordError=" + error)

    if verify_password == "":
        pushToResult = False
        error = "Verify Password field was empty!"
        return redirect("/?passwordVerifyError=" + error)

    if " " in password:
        pushToResult = False
        error = "Password had unsupported characters"
        return redirect("/?passwordError=" + error)

    if len(password) < 3:
        pushToResult = False
        error = "Password is too short"
        return redirect("/?passwordError=" + error)

    if len(password) > 20:
        pushToResult = False
        error = "Password is too long"
        return redirect("/?passwordError=" + error)

    if email != "":
        if any(["@" in email]):
            error = ""
        else:
            pushToResult = False
            error = "Email did not contain @ sign"
            return redirect("/?emailError=" + error)
        if any([" " in email]):
            pushToResult = False
            error = "Email cannot contain any spaces"
            return redirect("/?emailError=" + error)
        if any(["." in email]):
            error = ""
        else:
            pushToResult = False
            error = "Email did not contain any periods"
            return redirect("/?emailError=" + error)
        if len(email) < 3:
            pushToResult = False
            error = "Email is too short"
            return redirect("/?emailError=" + error)
        if len(email) > 20:
            pushToResult = False
            error = "Email is too long"
            return redirect("/?emailError=" + error)


    if verify_password != password:
        pushToResult = False
        error = "Verify Password did not match Password!"
        return redirect("/?passwordError=" + error)

    if pushToResult:
        return render_template('result_form.html', username=username) 
    #else:
    #    return redirect("/?error=" + error)

app.run()