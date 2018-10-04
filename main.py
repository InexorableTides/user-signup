from flask import Flask, request, redirect, render_template
import cgi


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

    if name.isalnum() and password == repeated and len(email) <= 20:
        
        return render_template("sucess.html", your_name=name)
    if name.isalnum() and password == repeated and len(email) > 20:
        mail_error = "This is not a valid E-mail!"
        return render_template("base.html", your_name=name, your_email=email, email_error=mail_error)
    if name.isalnum() and password != repeated:
        password_error = "The passwords are invalid"
        return render_template("base.html", your_name=name, your_email=email, password_error=password_error)
    else:
        name_error = "The username is invalid"
        return render_template("base.html", your_name=name, your_email=email, name_error=name_error)

app.run()