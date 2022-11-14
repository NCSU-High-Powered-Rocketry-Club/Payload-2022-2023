import RPi.GPIO as GPIO

# these are the pins we are connecting the antennas to
# TODO: Add which pins we are connecting to IN1 and IN2 on the relay
# I think they should be GPIO pins
antenna_1_pin = 11
antenna_2_pin = 13

# setup board
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# set output pins to output
GPIO.setup(antenna_1_pin, GPIO.OUT)
GPIO.setup(antenna_2_pin, GPIO.OUT)

# TODO: add code here to determine the antenna
antenna_num = 1
# antenna_num = 2

if antenna_num == 1:
    GPIO.output(antenna_2_pin, False)
    GPIO.output(antenna_1_pin, True)
elif antenna_num == 2:
    GPIO.output(antenna_1_pin, False)
    GPIO.output(antenna_2_pin, True)
