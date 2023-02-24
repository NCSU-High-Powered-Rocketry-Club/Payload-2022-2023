import imageFilter
import random
import RPi.GPIO as GPIO
import re
#from ServoLib import RocketServos
import takepicPDF
import moveServo
from PIL import Image

#example_APRS = "XX4XXX C3 A1 D4 C3 F6 C3 F6 B2 B2 C3"
#example_APRS = "XX4XXX C3 E5 C3 D4 C3 F6 B2 C3 B2 C3"
#APRS_clip = aprsMsg[7:]

def executeCmdsPDF():
    x = 0
    gray = 0
    randnum = 0
    pin = 22 # Change this to the correct pin that you'll use, you gotta test it
    APRS_clip = "C3 A1 D4 C3 F6 C3 F6 B2 B2 C3"
    cam = "pinky"
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin,GPIO.OUT)
    pwm = GPIO.PWM(pin, 50)
    while x < len(APRS_clip):
        if APRS_clip[x] == "A":
            moveServo.moveServo(60,pwm)
            print("A1")
        elif APRS_clip[x] == "B":
            moveServo.moveServo(-60,pwm)
            print("B2")
        elif APRS_clip[x] == "C":
            # Take picture
            takepicPDF.takepicPDF(cam, x)
            if gray == 1: # 1 if grayscale filter has been applied
                pic2gray = "capture_%s_%d.jpg" % (cam, x)
                pic2gray = imageFilter.blackandwhite(pic2gray)
                pic2gray.save("capture_%s_%d.jpg" % (cam, x))
            # If randnum~=0, then a random filter has been applied
            if randnum == 1: # deepfry
                pic2filter = "capture_%s_%d.jpg" % (cam, x)
                pic2filter = Image.open(r'/home/pi/Payload-2022-2023/%s' % pic2filter)
                pic2filter = imageFilter.fry(pic2filter)
                pic2filter.save("capture_%s_%d.jpg" % (cam, x))
            elif randnum == 2: # grassless
                pic2filter = "capture_%s_%d.jpg" % (cam, x)
                pic2filter = Image.open(r'/home/pi/Payload-2022-2023/%s' % pic2filter)
                pic2filter = imageFilter.grassless(pic2filter)
                pic2filter.save("capture_%s_%d.jpg" % (cam, x))
                print('Grassless filter applied')
            elif randnum == 3: # meme
                pic2filter = "capture_%s_%d.jpg" % (cam, x)
                pic2filter = Image.open(r'/home/pi/Payload-2022-2023/%s' % pic2filter)
                pic2filter = imageFilter.meme(pic2filter)
                pic2filter.save("capture_%s_%d.jpg" % (cam, x))
                print('Meme filter applied')
            elif randnum == 0: # Default, no filter
                print('No filter applied')
            else: # I dunno when this would happen I just had it in case
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
            pic2rotate = "capture_%s_%d.jpg" % (cam, x-3)
            pic2rotate = Image.open(r'/home/pi/Payload-2022-2023/%s' % pic2rotate) # Make sure this is right
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

executeCmdsPDF()
