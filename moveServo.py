import RPi.GPIO as GPIO
from time import sleep

# Set up GPIO mode as BOARD to reference the pin numbers
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinnum, GPIO.OUT) #This number refers to the pin the servo is connected to

# Create variable for servo, send 50 Hz PWM signal, starting at 0
pwm = GPIO.PWM(pinnum,50)
pwm.start(0)

# Allows main.py to set angle
def setAngle(angle,pinnum):
    duty = angle / 18 + 3
    GPIO.output(pinnum, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(pinnum, False)
    pwm.ChangeDutyCycle(duty)