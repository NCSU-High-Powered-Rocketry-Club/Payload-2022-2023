import Servo
import time

def testServo():
    myServo = Servo(33, 0, 100) # Define class Servo in this file
    myServo.set_degrees(0)
    time.sleep(3)
    myServo.set_degrees(180)
    time.sleep(3)

while True:
    testServo()