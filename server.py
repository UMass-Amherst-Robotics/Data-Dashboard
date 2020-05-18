# UMass Robotics Team
# Data-Dashboard Project
#
# server.py
#
# Created by CE/CS Team
# Created on May 15th, 2020

from flask import Flask, request, jsonify
from tinydb import TinyDB, Query

####################################
db = TinyDB('data.json')    # TinyDB Database
####################################
server = Flask(__name__)       # Server
####################################

# class Datastore:
#     def __init__(self,type):
#         if type == "TinyDB":
#             pass
#
#     def insert():
#         pass
#     def update():
#         pass


# example GET Request to retrieve data from server
@server.route('/', methods=['GET'])
def welcomeMessage():
    return jsonify({'message' : 'Welcome to the server!'})

# POST Request to send data to the server from robot
@server.route('/data', methods=['POST', 'GET'])
def addData():
    if request.method == 'POST':
        info = request.get_json()
        try:
            db.insert(info)
            for k,v in info.items():
                print("Key: {}, Value: {}".format(k,v))
            return "success"
        except:
            return "fail"
    else:
        data = db.all() # get all data from db
        last_row = data[len(data) - 1]
        return last_row


@server.route('/data/<n_records>')
def getDataNRecords(n_records):
    n = int(n_records)
    data = db.all()
    last_n = data[len(data) - 1 - n:]
    return {"records":last_n}

############### CHART GET REQUESTS ############################

# Here you can Enter all the get requests from the server to your CHART

if __name__ == '__main__':
    server.run()
