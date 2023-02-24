import RPI.GPIO as GPIO
from picamera import PiCamera
import time

def takepicPDF(cam, x):
    camera = PiCamera()
    time.sleep(2)
    camera.capture("/home/pi/Payload-2022-2023/capture_%s_%d.jpg" % (cam,x))