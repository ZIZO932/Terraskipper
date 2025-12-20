# Mudskipper Soft Robot Control Code
# Platform: Raspberry Pi Pico

import time

# -----------------------
# Mock / Abstracted Devices
# -----------------------

class Servo:
    def __init__(self, name):
        self.name = name
        self.angle = 90

    def move(self, angle):
        self.angle = angle
        print(f"{self.name} -> {angle}°")

class Sensor:
    def read(self):
        return None

# -----------------------
# Actuators
# -----------------------

LF = Servo("Left Front Leg")
RF = Servo("Right Front Leg")
LR = Servo("Left Rear Leg")
RR = Servo("Right Rear Leg")
TAIL = Servo("Tail")

PH_TUBE = Servo("pH Probe")
TDS_TUBE = Servo("TDS Probe")

# -----------------------
# Sensors (Conceptual)
# -----------------------

class Ultrasonic(Sensor):
    def read(self):
        return 25  # cm (example)

class PH(Sensor):
    def read(self):
        return 6.8

class TDS(Sensor):
    def read(self):
        return 1200  # ppm

class GPS(Sensor):
    def read(self):
        return ("30.0N", "31.0E")

ultrasonic = Ultrasonic()
ph_sensor = PH()
tds_sensor = TDS()
gps = GPS()

# -----------------------
# Movement Logic
# -----------------------

def mudskipper_step(phase):
    if phase == 0:
        LF.move(120)
        RR.move(120)
        RF.move(60)
        LR.move(60)
    else:
        RF.move(120)
        LR.move(120)
        LF.move(60)
        RR.move(60)

    TAIL.move(110)
    time.sleep(0.2)
    TAIL.move(70)
    time.sleep(0.2)

    # Reset posture
    for leg in [LF, RF, LR, RR, TAIL]:
        leg.move(90)

# -----------------------
# Soil Measurement Logic
# -----------------------

def take_soil_measurements():
    print("Deploying probes...")
    PH_TUBE.move(40)
    TDS_TUBE.move(40)
    time.sleep(1)

    ph = ph_sensor.read()
    tds = tds_sensor.read()
    location = gps.read()

    PH_TUBE.move(90)
    TDS_TUBE.move(90)

    data = {
        "pH": ph,
        "TDS_ppm": tds,
        "location": location
    }

    print("Soil Data:", data)

# -----------------------
# Main Loop
# -----------------------

phase = 0
last_measurement = time.time()

print("Mudskipper robot logic initialized")

while True:
    mudskipper_step(phase)
    phase = 1 - phase

    if time.time() - last_measurement > 5:
        last_measurement = time.time()

        distance = ultrasonic.read()
        print("Obstacle distance:", distance, "cm")

        take_soil_measurements()

    time.sleep(0.1)
