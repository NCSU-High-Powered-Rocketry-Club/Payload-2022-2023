import RPi.GPIO as GPIO
import BNOInterface

# Necessary to prevent import issues on APRSInterface
import sys
sys.path.append("./aprs_decoding/test")

from APRSInterface import APRSInterface

# these are the GPIO pins we are controlling the relay switch with
ANTENNA_1_PIN = 17
ANTENNA_2_PIN = 27

def main():
    aprs_interface = APRSInterface()

    choose_antenna()

    aprs_interface.startRecv()

    try:
        while True:
            # chooseAntenna()
            pass
    except KeyboardInterrupt:
        pass

    aprs_interface.stop()

def choose_antenna():
    sensor = BNOInterface.BNOInterface()

    # setup board
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # set output pins to output
    GPIO.setup(ANTENNA_1_PIN, GPIO.OUT)
    GPIO.setup(ANTENNA_2_PIN, GPIO.OUT)

    #setup orientation determination
    angle = 0
    # TODO: Make sure we know how the IMU is oriented before calling z
    print('IMU ORIENTATION HAS NOT BEEN CONFIRMED')
    angle = sensor.get_euler()[2] #using the z-axis euler angle to determine orientation
    print(angle)

    if angle in range(0, 135) or angle in range (315, 360):
        GPIO.output(ANTENNA_2_PIN, True)
        GPIO.output(ANTENNA_1_PIN, False)

        print("Chose antenna 2")
    elif angle in range(135, 315):
        GPIO.output(ANTENNA_1_PIN, True)
        GPIO.output(ANTENNA_2_PIN, False)

        print("Chose antenna 1")

if __name__ == "__main__":
    main()
