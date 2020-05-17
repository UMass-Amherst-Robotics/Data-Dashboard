from flask import Flask, render_template

app = Flask(__name__)

# route = endpoint
@app.route('/')
def hello_world():
    currentSpeedPython = 75
    averageSpeedPython = 50
    totalDistancePython = 100
    currentVoltagePython = 4.8
    averageVoltagePython = 5.6
    batteryLifePython = 70
    currentCPUTemperaturePython = 95
    averageCPUTemperaturePython = 105
    currentSensorTemperaturePython = 100
    averageSensorTemperaturePython = 90
    frontRightWheelStressPython = 2
    frontLeftWheelStressPython = 1
    backRightWheelStressPython = 3
    backLeftWheelStressPython = 4
    return render_template("views/index.html", currentSpeedHTML=currentSpeedPython, averageSpeedHTML=averageSpeedPython, totalDistanceHTML=totalDistancePython, currentVoltageHTML=currentVoltagePython, averageVoltageHTML=averageVoltagePython, batteryLifeHTML=batteryLifePython, currentCPUTemperatureHTML=currentCPUTemperaturePython, averageCPUTemperatureHTML=averageCPUTemperaturePython, currentSensorTemperatureHTML=currentSensorTemperaturePython, averageSensorTemperatureHTML=averageSensorTemperaturePython, frontRightWheelStressHTML=frontRightWheelStressPython, frontLeftWheelStressHTML=frontLeftWheelStressPython, backRightWheelStressHTML=backRightWheelStressPython, backLeftWheelStressHTML=backLeftWheelStressPython)
    # don't need "template/" because Flask objeect looks for template folder

if __name__ == "__main__":
    app.run(debug=True)