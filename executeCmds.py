import imageFilter
import random
import RPi.GPIO as GPIO
import re
import takepic
from ServoLib import RocketServos
from PIL import Image
import moveServo
import asyncio

#example_APRS = "XX4XXX C3 A1 D4 C3 F6 C3 F6 B2 B2 C3"
#example_APRS = "XX4XXX C3 E5 C3 D4 C3 F6 B2 C3 B2 C3"
#APRS_clip = aprsMsg[7:]

def executeCmds(APRS_clip, cam):
    x = 0
    gray = 0
    randnum = 0
    print("Executing Commands")
    if cam == "big":
        pinCam = 33
        pinServo = 0
    elif cam == "pinky":
        pinCam = 0 # Change
        pinServo = 0
    elif cam == "ring":
        pinCam = 0 # Change
        pinServo = 0
    elif cam == "jahn":
        pinCam = 0 # Change
        pinServo
    else:
        print("No pin assigned for Servo")

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinServo,GPIO.OUT)
    pwm = GPIO.PWM(pinServo, 50)

    while x < len(APRS_clip):
        if APRS_clip[x] == "A":
            moveServo(-60,pwm)
            print("A1")
        elif APRS_clip[x] == "B":
            moveServo(-60,pwm)
            print("B2")
        elif APRS_clip[x] == "C":
            # Take picture
            takepic.takepic(cam, x)
            if gray == 1: # 1 if grayscale filter has been applied
                pic2gray = Image.open(f"capture_{cam}_{x}.jpg")
                pic2gray = imageFilter.blackandwhite(pic2gray)
                pic2gray.save(f"capture_{cam}_{x}.jpg")
            # If randnum~=0, then a random filter has been applied
            if randnum == 1: 
                #pic2filter = "capture_%s_%d.jpg" % (cam, x)
                #pic2filter = imageFilter.fry(pic2filter)
                #pic2filter.save("capture_%s_%d.jpg" % (cam, x))
                print('whoops cant fry lol')
            elif randnum == 2:
                pic2filter = Image.open(f"capture_{cam}_{x}.jpg")
                pic2filter = imageFilter.grassless(pic2filter)
                pic2filter.save(f"grassless_{cam}_{x}.jpg")
            elif randnum == 3:
                pic2filter = Image.open(f"capture_{cam}_{x}.jpg")
                pic2filter = imageFilter.meme(pic2filter)
                pic2filter.save(f"meme_{cam}_{x}.jpg")
            else:
                print('Your RNG is broken')
            print("C3")
        elif APRS_clip[x] == "D":
            # Change camera mode from grayscale to color
            gray = 0
            print("D4")
        elif APRS_clip[x] == "E":
            # Change camera mode from color to grayscale
            gray = 1
            print("E5")
        elif APRS_clip[x] == "F":
            # Rotate image 180deg
            pic2rotate = Image.open(f"capture_{cam}_{x-3}.jpg")
            pic2rotate = imageFilter.rotate180(pic2rotate)
            pic2rotate.save("capture_%s_%d.jpg" % (cam, x))
            print("F6")
        elif APRS_clip[x] == "G":
            # Special effects filter
            print("G7")
            randnum = random.randint(1,3)
        elif APRS_clip[x] == "H":
            randnum = 0
            gray = 0
            print("H8")
        else:
            print("You done fucked up chief")
        x = x + 3
