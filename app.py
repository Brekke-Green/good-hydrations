from flask import Flask, render_template, request
import os
from time import  time

app = Flask(__name__)

plants_data = {
        "alocasia": ["2023/07/08/-08:00:00", "2023/07/20/-08:00:00", "2023/08/3/-08:00:00"],
        "hedgehog aloe": ["2023/07/12/-08:00:00", "2023/07/18/-08:00:00"],
        "pothos": ["2023/07/12/-08:00:00", "2023/07/14/-08:00:00", "2023/07/20/-08:00:00"],
        }

logged_in = False

@app.route("/")
def home():
    return render_template('index.html', logged_in=logged_in)

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/login")
def login():
    global logged_in 
    logged_in = True
    return render_template('login.html', logged_in=logged_in)

@app.route("/plants")
def plants():
    return render_template('plants.html', plants=plants_data)

####NOT FUNCTIONAL - continue to build out selecting individual plant and reporting logs/data
##@app.route("/plants/<name>")
##def plant(name):
##    plant_logs = plants_data[name] 
##    return render_template('plants.html', plant=name, logs=plant_logs)

if  __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

