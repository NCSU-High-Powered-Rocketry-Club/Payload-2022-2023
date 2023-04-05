from picamera import PiCamera
import time

def takepic(cam, x):
    camera = PiCamera()
    stringy = f"capture_{cam}_{x}.jpg"
    camera.capture(stringy)
    print("Captured image")
