from flask import Flask, render_template
import os
from time import  time

app = Flask(__name__)

plants = {"alocasia": ["2023/07/08/-08:00:00"]}

@app.route("/")
def home():
    return render_template('index.html', plants=plants)

@app.route("/signup")
def signup():
    return render_template('signup.html')

if  __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

