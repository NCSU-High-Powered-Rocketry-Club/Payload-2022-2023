#from PIL import Image
import imageFilter
import random
import re
import Servo

#example_APRS = "XX4XXX C3 A1 D4 C3 F6 C3 F6 B2 B2 C3"
#APRS_clip = aprsMsg[7:]

def executeCmds(APRS_clip, cam):
    myServo = Servo(33, 0, 100) # Define class Servo in this file
    x = 0
    cam.color_effects = None
    while x < len(APRS_clip):
        if APRS_clip[x] == "A":
            if x != 0:
                # Save the previously captured image if there is one
                return 1
            else:
                myServo.set_degrees(60) #need to define GPIO pins the servo's attached to
            print("A1")
        elif APRS_clip[x] == "B":
            if x != 0:
                # Save the previously captured image if there is one
                return 1
            else:
                # Turn servo 60deg to the left
                myServo.set_degrees(-60) #need to define GPIO pins the servo's attached to
            print("B2")
        elif APRS_clip[x] == "C":
            # Save the previously captured image if there is one (ie if x ~=0)
            # Take picture
            #image = Image.open("pic.jpg") # Placeholder for actual captured image
            print("C3")
        elif APRS_clip[x] == "D":
            # Change camera mode from grayscale to color
            cam.color_effects = None
            print("D4")
        elif APRS_clip[x] == "E":
            # Change camera mode from color to grayscale
            cam.color_effects = (128, 128)
            print("E5")
        elif APRS_clip[x] == "F":
            # Rotate image 180deg
            print("F6")
            #imageFilter.rotate180(image)
        elif APRS_clip[x] == "G":
            # Special effects filter
            print("G7")
            randnum = random.randint(1,3)
            if randnum == 1:
                print("1")
                #imageFilter.fry(image)
            elif randnum == 2:
                print("2")
                #imageFilter.grassless(image)
            elif randnum == 3:
                print("3")
                #imageFilter.meme(image)
            else:
                print("Your RNG is broken")
        elif APRS_clip[x] == "H":
            # Remove all filters
            print("H8")
        else:
            print("You done fucked up chief")
        x = x + 3
