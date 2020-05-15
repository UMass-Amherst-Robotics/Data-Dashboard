# UMass Robotics Team
# Data-Dashboard Project
#
# app.py
#
# Created by CE/CS Team
# Created on May 15th, 2020

import requests

serverAddr = 'http://127.0.0.1:5000/'

response = requests.get(serverAddr)
print(response.json())
