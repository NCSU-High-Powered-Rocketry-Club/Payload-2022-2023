import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19,GPIO.OUT)

GPIO.output(19,True)