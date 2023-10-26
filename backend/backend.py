from flask import Flask, request
from faslk_cors import CORS
import joblib

app = Flask(__name__)

@app.route("/hola", methods=["GET"])
def inicio():
    return "Hola mundo"


if __name =="__main__":
    app.run (host="0.0.0.0", debug =False, port=8081)

