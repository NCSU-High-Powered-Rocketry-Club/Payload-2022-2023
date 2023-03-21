import RPi.GPIO as GPIO
import re
import moveServo
import time

GPIO.setmode(GPIO.BOARD)

pinServo = 24
GPIO.setup(pinServo, GPIO.OUT)
pwm = GPIO.PWM(pinServo, 500)
moveServo.moveServo(60, pwm)
moveServo.moveServo(-60, pwm)
time.sleep(2)

pinServo = 21
GPIO.setup(pinServo, GPIO.OUT)
pwm = GPIO.PWM(pinServo, 500)
moveServo.moveServo(60, pwm)
moveServo.moveServo(-60, pwm)
time.sleep(2)

pinServo = 23
GPIO.setup(pinServo, GPIO.OUT)
pwm = GPIO.PWM(pinServo, 500)
moveServo.moveServo(60, pwm)
moveServo.moveServo(-60, pwm)
time.sleep(2)

pinServo = 22
GPIO.setup(pinServo, GPIO.OUT)
pwm = GPIO.PWM(pinServo, 500)
moveServo.moveServo(60, pwm)
moveServo.moveServo(-60, pwm)
time.sleep(2)
