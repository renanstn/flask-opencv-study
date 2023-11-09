from flask import Flask, render_template, send_file, request
from werkzeug.utils import secure_filename
import cv2


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file_path = f"{app.config['UPLOAD_FOLDER']}/{filename}"
        file.save(file_path)
        imgage = cv2.imread(file_path)
        gray_image = cv2.cvtColor(imgage, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(file_path, gray_image)
        return render_template("index.html", filename=filename)

@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    try:
        file_path = f"{app.config['UPLOAD_FOLDER']}/{filename}"
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return str(e)
