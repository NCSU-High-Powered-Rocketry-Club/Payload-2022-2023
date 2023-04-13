from picamera import PiCamera
import time

def takepic(cam, x, folder_name):
    camera = PiCamera()
    stringy = f"{folder_name}capture_{cam}_{x}.jpg"
    camera.capture(stringy)
    print("Captured image")
    camera.close()
