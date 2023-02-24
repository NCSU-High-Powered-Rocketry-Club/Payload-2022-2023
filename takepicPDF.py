import RPi.GPIO as gp
import os

def takepicPDF(cam, x):
    cmd = "libcamera-still -n -o capture_%s_%d.jpg" % (cam, x)
    os.system(cmd)