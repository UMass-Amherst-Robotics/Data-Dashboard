# UMass Robotics Team
# Data-Dashboard Project
#
# server.py
#
# Created by CE/CS Team
# Created on May 15th, 2020

from flask import Flask
from flask import request
from flask import jsonify
from tinydb import TinyDB, Query

####################################
db = TinyDB('data.json')    # TinyDB Database
####################################
server = Flask(__name__)       # Server
####################################

# example GET Request to retrieve data from server
@server.route('/', methods=['GET'])
def welcomeMessage():
    return jsonify({'message' : 'Weclome to the server!'})

# POST Request to send data to the server from robot
@server.route('/data', methods=['POST'])
def addData():
    db.insert(request.get_json())
    return ""

############### CHART GET REQUESTS ############################

# Here you can Enter all the get requests from the server to your CHART

if __name__ == '__main__':
    server.run()
