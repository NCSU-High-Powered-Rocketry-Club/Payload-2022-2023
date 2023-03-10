import RPi.GPIO as GPIO
import re
import moveServo

GPIO.setmode(GPIO.BOARD)

pinServo = 24
GPIO.setup(pinServo,GPIO.OUT)
pwm = GPIO.PWM(pinServo, 50)
moveServo(60, pwm)

pinServo = 21
GPIO.setup(pinServo,GPIO.OUT)
pwm = GPIO.PWM(pinServo, 50)
moveServo(60, pwm)

pinServo = 23
GPIO.setup(pinServo,GPIO.OUT)
pwm = GPIO.PWM(pinServo, 50)
moveServo(60, pwm)

pinServo = 22
GPIO.setup(pinServo,GPIO.OUT)
pwm = GPIO.PWM(pinServo, 50)
moveServo(60, pwm)
