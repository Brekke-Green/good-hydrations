from flask import Flask, render_template
import os
from time import  time

app = Flask(__name__)

plants_data = {
        "alocasia": ["2023/07/08/-08:00:00", "2023/07/20/-08:00:00"],
        "hedgehog aloe": ["2023/07/12/-08:00:00", "2023/07/18/-08:00:00"],}

logged_in = False

@app.route("/")
def home():
    return render_template('index.html', logged_in=logged_in)

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/plants")
def plants():
    return render_template('plants.html', plants=plants_data)

if  __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

