from flask import Flask, render_template, request

from helpers import generate_password

# Configure application
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/new-password", methods=["POST"])
def new_password():

    # Generate new password
    if request.method == "POST":
        length = int(request.form.get("length"))
        new_password = generate_password(length)
        return render_template("new_password.html", new_password=new_password)
