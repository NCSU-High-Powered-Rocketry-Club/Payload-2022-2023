import RPi.GPIO as GPIO
from Servo import Servo
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
pwm = GPIO.PWM(18, 50)
pwm.start(50)

def testServo():
    print('0')
    pwm.ChangeDutyCycle(100)
    print('100')

while True:
    testServo()