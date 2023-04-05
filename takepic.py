from picamera import PiCamera
import time

camera = PiCamera()
time.sleep()

camera.capture("/home/pi/Payload-2022-2023/img.jpg")
print("hee hee hoo hoo")