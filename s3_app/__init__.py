from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_object("s3_app.config")

from .helpers import *

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def upload_file():

    if "select_file" not in request.files:
        return "Please return to previous page and select a file"

    file = request.files["select_file"]

    if file.filename == "":
        return "Please return to previous page and select a file"

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        output = upload_file_to_s3(file, app.config["S3_BUCKET"])
        return output

    else:
        return redirect("/")
