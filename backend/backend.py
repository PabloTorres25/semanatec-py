from flask import Flask, request
from flask_cors import CORS

import joblib
import os

dt = joblib.load("./static/dt.joblib")

app = Flask(__name__)
CORS(app)

@app.route("/hola", methods=["GET"])
def inicio():
    return "Hola mundo"

@app.route("/predict_json", methods=["POST"])
def predict_json():
    data = request.json
    X = [
        data["pH"],
        data["sulphates"],
        data["alcohol"]
        ]
    y_pred = dt.predict(X)
    # print(y_pred)
    return jsonify({"result": y_pred[0]})

# Lo sacamos de form en ves de de json
@app.route("/predict_form", methods=["POST"])
def predict_form():
    data = request.form
    X = [
        data["pH"],
        data["sulphates"],
        data["alcohol"]
        ]
    y_pred = dt.predict(X)
    # print(y_pred)
    return jsonify({"result": y_pred[0]})

@app.route("/predict_file", methods=["POST"])
def predict_file():
    files = request.files["archivo"]
    filename = secure_filename(file.filename)
    # file.save(f"./static/{filename}")           # Manera poco segura de generar el archivo
    file.save(os.path.join(os.getcwd(), "static", filename))    # Manera segura


if __name =="__main__":
    app.run (host="0.0.0.0", debug =False, port=8081)

