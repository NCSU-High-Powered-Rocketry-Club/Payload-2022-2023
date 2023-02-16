from picamera import PiCamera

camera = PiCamera()
def takepic():
    camera.start_preview()
    camera.capture('/home/pi/Payload-2022-2023/image.jpg')
    print('Hello world')
    camera.stop_preview()