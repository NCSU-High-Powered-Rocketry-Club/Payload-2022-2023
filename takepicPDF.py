import RPi.GPIO as GPIO
import libcamera
import os
import numpy as np
from PIL import Image
import time
import cv2

def takepicPDF(cam, x):
    camera = libcamera.Camera()
    camera.start()
    buffer = camera.capture()
    image_data = np.frombuffer(buffer, dtype=np.uint8)
    image_
    time.sleep(2)
    image = rawCapture.array
