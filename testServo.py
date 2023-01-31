from Servo import Servo
import time

def testServo():
    myServo = Servo(13, 1, 50) # Define class Servo in this file
    myServo.set_degrees(0)
    time.sleep(3)
    myServo.set_degrees(180)
    time.sleep(3)

while True:
    testServo()