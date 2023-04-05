from picamera import PiCamera
import time

camera = PiCamera()
time.sleep(1)

camera.capture("/home/pi/Payload-2022-2023/img.jpg")
print("hee hee hoo hoo")
