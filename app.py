from flask import Flask
from time import  time

app = Flask(__name__)

plants = {"alocasia": ["2023/07/08/-08:00:00"]}

@app.route("/")
def hello_world():
    return f"ENJOY SOME GOOD HYDRATIONS \n {plants}"

