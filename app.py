from flask import Flask, render_template, request, redirect
import os
from time import  time

app = Flask(__name__)

plants_data = {
        "alocasia": ["2023/07/08/-08:00:00", "2023/07/20/-08:00:00", "2023/08/03/-08:00:00"],
        "hedgehog_aloe": ["2023/07/12/-08:00:00", "2023/07/18/-08:00:00"],
        "pothos": ["2023/07/12/-08:00:00", "2023/07/14/-08:00:00", "2023/07/20/-08:00:00"],
        "anthurium": ["2023/08/06/-08:00:00"],
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
    plant_urls = generate_urls(plants_data)
    plants_length = len(plants_data.keys())
    return render_template('plants.html', plants=plants_data, plant_urls=plant_urls, plants_length=plants_length)

def generate_urls(plants_data):
    result = {}
    for key in plants_data.keys():
        result[key] = f"/plants/{key}"
    return result

@app.route("/plants/<name>")
def plant(name):
    plant_log = {name: plants_data[name]}
    plant_urls = generate_urls(plant_log)
    return render_template('plants.html', plants=plant_log, plant_urls=plant_urls, plants_length=1)

if  __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

