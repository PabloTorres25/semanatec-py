from flask import Flask, request
from flask_cors import CORS
import joblib

dt = joblib.load("/static/dt.joblib")

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

if __name =="__main__":
    app.run (host="0.0.0.0", debug =False, port=8081)

