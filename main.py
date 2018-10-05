from flask import Flask, request, redirect, render_template
import cgi
import re


app = Flask(__name__)

app.config['DEBUG'] = True 


@app.route("/")
def index():
    return render_template("base.html", your_name="", your_email="", name_error="", password_error="", email_error="")


@app.route("/validate_login", methods=['POST'])
def validation():
    name = request.form['username']
    password = request.form['password']
    repeated = request.form['verify']
    email = request.form['email']
    name = str(name)
    password = str(password)
    repeated = str(repeated)
    email = str(email)
    email_regex = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")

    if len(name) < 3:
        name_error = "The username is too short(between 3-20 characters)"
        return render_template("base.html", your_name=name, your_email=email, name_error=name_error)
    if len(name) > 20:
        name_error = "The username is too long(between 3-20 characters)"
        return render_template("base.html", your_name=name, your_email=email, name_error=name_error)
    if name.isalnum() and password == repeated and len(email) > 20:
        email_error = "E-Mail is too long!(between 3-20 characters)"
        return render_template("base.html", your_name=name, your_email=email, email_error=email_error)
    if name.isalnum() and password == repeated and len(password) > 20:
        password_error = "Password is too long!(between 3 and 20 Characters)"
        return render_template("base.html", your_name=name, your_email=email, password_error=password_error )
    if name.isalnum() and password == repeated and len(password) < 3:
        password_error = "Password is too short!(between 3 and 20 Characters)"
        return render_template("base.html", your_name=name, your_email=email, password_error=password_error)     
    if name.isalnum() and password == repeated and len(repeated) > 20:
        password_error = "Password is too long!(between 3 and 20 Characters)"
        return render_template("base.html", your_name=name, your_email=email ,password_error=password_error )
    if name.isalnum() and password == repeated and len(repeated) < 3:
        password_error = "Password is too short!(between 3 and 20 Characters)"
        return render_template("base.html", your_name=name, your_email=email, password_error=password_error)     
     
    
    if name.isalnum() and password == repeated and len(email) < 3:
        email_error = "E-mail is too short!(between 3-20 characters)"
        return render_template("base.html", your_name=name, your_email=email, email_error=email_error)     
    if name.isalnum() and password == repeated and len(email) :
        if not email_regex.match(email): 
            email_error = "This is not a valid E-mail!"
            return render_template("base.html", your_name=name, your_email=email, email_error=email_error)
        if email_regex.match(email):
            return render_template("sucess.html", your_name=name)
            
    if name.isalnum() and password != repeated:
        password_error = "The passwords do not match!"
        return render_template("base.html", your_name=name, your_email=email, password_error=password_error)
    else:
        name_error = "The username is invalid(cannot contain spaces or non alphanumerics)"
        return render_template("base.html", your_name=name, your_email=email, name_error=name_error)

app.run()