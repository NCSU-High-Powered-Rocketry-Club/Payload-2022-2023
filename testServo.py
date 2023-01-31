import RPi.GPIO as GPIO
from Servo import Servo
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
pwm = GPIO.PWM(18, 1000)
pwm.start(50)

def testServo():
    pwm.ChangeDutyCycle(0)
    print('0')
    time.sleep(3)
    pwm.ChangeDutyCycle(100)
    print('100')
    time.sleep(3)

while True:
    testServo()