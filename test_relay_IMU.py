import RPi.GPIO as GPIO
import BNOInterface

# these are the pins we are connecting the antennas to
# TODO: Add which pins we are connecting to IN1 and IN2 on the relay
def main():
    sensor = BNOInterface.BNOInterface()
    antenna_1_pin = 11
    antenna_2_pin = 13

    # setup board
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # set output pins to output
    GPIO.setup(antenna_1_pin, GPIO.OUT)
    GPIO.setup(antenna_2_pin, GPIO.OUT)

    #setup orientation determination
    angle = 0
    angle = sensor.get_euler()[2] #using the z-axis euler angle to determine orientation

    if angle in range(0, 135):
        antenna_num = 1
    elif angle in range(135, 315):
        antenna_num = 2
    elif angle in range(315, 360):
        antenna_num = 1


    #NOTE: Relay activates on LOW, i.e. FALSE
    if antenna_num == 1:
        GPIO.output(antenna_2_pin, True)
        GPIO.output(antenna_1_pin, False)
    elif antenna_num == 2:
        GPIO.output(antenna_1_pin, True)
        GPIO.output(antenna_2_pin, False)


if __name__ == "__main__":
    main()
