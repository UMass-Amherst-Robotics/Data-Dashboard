# UMass Robotics Team
# Data-Dashboard Project
#
# app.py
#
# Created by CE/CS Team
# Created on May 15th, 2020

from flask import Flask, request, jsonify, render_template
import os
import requests
import json

####################################
app = Flask(__name__)       # Server
####################################

# example GET Request to retrieve data from server
@app.route('/')
def get_data():
    r = requests.get("http://localhost:5000/data")
    data = json.loads(r.text)

    return render_template('views/index.html',data=data)


@app.route('/historical/<n>')
def get_history(n):
    r = requests.get("http://localhost:5000/data/"+str(n))
    data = json.loads(r.text)
    print(data)
    return render_template('views/historical.html')

if __name__ == '__main__':
    app.run(port=5001)
