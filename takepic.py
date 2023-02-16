from picamera import PiCamera

camera = PiCamera()
camera.start_preview()
camera.capture('/home/pi/Payload-2022-2023/image.jpg')
camera.stop_preview()