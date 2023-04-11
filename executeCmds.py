import imageFilter
import random
import RPi.GPIO as GPIO
import re
import takepic
#from ServoLib import RocketServos
from PIL import Image
import moveServo
import asyncio
from datetime import datetime
import timeStamper

#example_APRS = "XX4XXX C3 A1 D4 C3 F6 C3 F6 B2 B2 C3"
#example_APRS = "XX4XXX C3 E5 C3 D4 C3 F6 B2 C3 B2 C3"
#APRS_clip = aprsMsg[7:]

def executeCmds(APRS_clip, cam):
    # Initialize filter variables
    x = 0
    gray = 0
    randnum = 0
    numTurns = 0 # no. times turned 60 deg clockwise

    # Executing commands
    print("Executing Commands")

    pinServo = 8
    
    # Servo pins based on 
    #if cam == "big":
    #    pinServo = 22
    #elif cam == "pinky":
    #    pinServo = 23
    #elif cam == "ring":
    #    pinServo = 21
    #elif cam == "jahn":
    #    pinServo = 24
    #else:
    #    pinServo = 22 # big = default
    #    print("No pin assigned for servo, green servo chosen")

    #GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinServo,GPIO.OUT)
    pwm = GPIO.PWM(pinServo, 500)

    while x < len(APRS_clip):
        if APRS_clip[x] == "A": # Move servo +60 deg
            if numTurns >= 3:
                moveServo.moveServo(-300,pwm)
                numTurns = numTurns - 5
            else:
                moveServo.moveServo(60,pwm)
                numTurns = numTurns + 1
            print("A1")
        
        elif APRS_clip[x] == "B": # Move servo -60 deg
            if numTurns <= -3:
                moveServo.moveServo(300,pwm)
                numTurns = numTurns + 5
            else:
                moveServo.moveServo(-60,pwm)
                numTurns = numTurns - 1
            print("B2")
        
        elif APRS_clip[x] == "C": # Take picture
            takepic.takepic(cam, x)
            currentTime = datetime.now()
            picName = f"capture_{cam}_{x}.jpg" # Current image path name
            timeStamper.timeStamper(currentTime, picName) # Replace unfiltered img w/ timestamped image
            
            if gray == 1: # 1 if grayscale filter applied
                pic2gray = Image.open(picName)
                pic2gray = imageFilter.blackandwhite(pic2gray)
                pic2gray.save(f"gray_{cam}_{x}.jpg")
                picName = f"gray_{cam}_{x}.jpg" # Current image path name
            
            # If randnum~=0, then a random filter has been applied
            if randnum == 1:
                #pic2filter = "capture_%s_%d.jpg" % (cam, x)
                #pic2filter = imageFilter.fry(pic2filter)
                #pic2filter.save("capture_%s_%d.jpg" % (cam, x))
                print('whoops cant fry lol')
            elif randnum == 2:
                pic2filter = Image.open(picName)
                pic2filter = imageFilter.grassless(pic2filter)
                pic2filter.save(f"grassless_{cam}_{x}.jpg")
                picName = f"grassless_{cam}_{x}.jpg" # Current image path name
            elif randnum == 3:
                pic2filter = Image.open(picName)
                pic2filter = imageFilter.meme(pic2filter)
                pic2filter.save(f"meme_{cam}_{x}.jpg")
                picName = f"meme_{cam}_{x}.jpg" # Current image path name
            else:
                print('Your RNG is broken')
            timeStamper.timeStamper(currentTime, picName) # Replace unfiltered img w/ timestamped image
            print("C3")
        
        elif APRS_clip[x] == "D": # Grayscale to color
            gray = 0
            print("D4")

        elif APRS_clip[x] == "E": # Color to grayscale
            gray = 1
            print("E5")

        elif APRS_clip[x] == "F": # Rotate image 180deg
            #pic2rotate = Image.open(f"capture_{cam}_{x-3}.jpg")
            pic2rotate = Image.open(picName)
            pic2rotate = imageFilter.rotate180(pic2rotate)
            pic2rotate.save("capture_%s_%d.jpg" % (cam, x))
            print("F6")

        elif APRS_clip[x] == "G": # Special effects filter
            print("G7")
            randnum = random.randint(2,3)

        elif APRS_clip[x] == "H": # Clear all filters
            randnum = 0
            gray = 0
            print("H8")

        else:
            print("Either indexing is wrong or the received msg is off-center")
        x = x + 3
