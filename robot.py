# UMass Robotics Team
# Data-Dashboard Project
#
# robot.py
#
# Created by CE/CS Team
# Created on May 15th, 2020
import psutil as ps
import requests
import time
import random

serverAddr = 'http://127.0.0.1:5000/data'
data_dict = {}

def update():
    data_dict["loadavg"] = ps.getloadavg()
    data_dict["cpu_percent"] = ps.cpu_percent()
    data_dict["virtual_memory"] = ps.virtual_memory()
    data_dict["battery_percentage"] = getBatteryPercentage()
    data_dict["time_stamp"] = time.time()

######### BATTERY PERCENTAGE EXAMPLE CODE FOR ROBOT ###########
# Definition: Returns the battery percentage of the robot over time.
# Function getBatteryPercentage() -> void
batteryPercentage = 101 # Fake Value
def getBatteryPercentage():
    # Fake example until we can get the real thing working on robot
    global batteryPercentage
    batteryPercentage = (batteryPercentage - 1)
    return batteryPercentage

# MARK: Main Method
if __name__ == '__main__':
    while(1):
        update()
        r = requests.post(serverAddr, json = data_dict)
        if r.text == "success":
            time.sleep(2)
        else:
            print("ERROR pushing data")
            time.sleep(2)
