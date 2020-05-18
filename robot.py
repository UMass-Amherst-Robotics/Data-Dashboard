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

# import sensor_pack

serverAddr = 'http://127.0.0.1:5000/data'

data_dict = {}
peen_sizes = ["small","substantial","massive","guti"]
def update():
    data_dict["loadavg"] = ps.getloadavg()
    data_dict["cpu_percent"] = ps.cpu_percent()
    data_dict["virtual_memory"] = ps.virtual_memory()
    data_dict["time_stamp"] = time.time()
    data_dict["peen"] = peen_sizes[random.randint(0,len(peen_sizes)-1)]

# data_dict["cpu_temperature"] = sensor_pack.cpu_temperature()

if __name__ == '__main__':
    while(1):
        update()
        r = requests.post(serverAddr, json = data_dict)
        if r.text == "success":
            time.sleep(2)
        else:
            print("ERROR pushing data")
            time.sleep(2)
