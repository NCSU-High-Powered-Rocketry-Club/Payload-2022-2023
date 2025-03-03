#from PIL import Image
#import imageFilter
import random
import RPi.GPIO as GPIO
import re
from ServoLib import RocketServos
#imort takepic
import moveServo
#from PIL import Image

#example_APRS = "XX4XXX C3 A1 D4 C3 F6 C3 F6 B2 B2 C3"
#example_APRS = "XX4XXX C3 E5 C3 D4 C3 F6 B2 C3 B2 C3"
#APRS_clip = aprsMsg[7:]

def executeServo():
    #myServo = Servo.Servo(33, 0, 100) # Define class Servo in this file
    APRS_clip = "C3 A1 D4 C3 F6 C3 F6 B2 B2 C3"
    cam = "pinky"
    x = 0
    pin = 19 # Change this to the correct pin number (choose it)
    print("Running")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin,GPIO.OUT)
    pwm = GPIO.PWM(pin, 50)
    moveServo.moveServo(60, "pinky", pwm)
    while x < len(APRS_clip):
        if APRS_clip[x] == "A":
            #moveServo.moveServo(60,cam,pwm)
            print("A1")
        elif APRS_clip[x] == "B":
            #moveServo.moveServo(-60,cam,pwm) # These degrees/duty cycles are wrong, change them
            print("B2")
        elif APRS_clip[x] == "C":
            # Take picture
            print("C3")
        elif APRS_clip[x] == "D":
            # Change camera mode from grayscale to color
            print("D4")
        elif APRS_clip[x] == "E":
            # Change camera mode from color to grayscale
            print("E5")
        elif APRS_clip[x] == "F":
            # Rotate image 180deg
            print("F6")
        elif APRS_clip[x] == "G":
            # Special effects filter
            print("G7")
        elif APRS_clip[x] == "H":
            print("H8")
        else:
            print("You done fucked up chief")
        x = x + 3

executeServo()
