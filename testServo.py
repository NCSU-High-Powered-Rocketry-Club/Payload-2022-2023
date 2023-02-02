import RPi.GPIO as GPIO
from Servo import Servo
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19,GPIO.OUT)
pwm = GPIO.PWM(19, 50)
pwm.start(0)

def testServo():
    print('0')
    pwm.ChangeDutyCycle(5)
    print('5')
    pwm.ChangeDutyCycle(7.5)
    print(7.5)
    pwm.ChangeDutyCycle(10)

while True:
    testServo()