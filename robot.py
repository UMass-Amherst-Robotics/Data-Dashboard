# UMass Robotics Team
# Data-Dashboard Project
#
# robot.py
#
# Created by CE/CS Team
# Created on May 15th, 2020

import requests

serverAddr = 'http://127.0.0.1:5000/data'

for i in range(4):
    response = requests.post(serverAddr, json={"batteryLevel": str(i)})
