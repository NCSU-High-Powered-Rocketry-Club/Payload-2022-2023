import RPi.GPIO as GPIO
from BNOInterface import BNOInterface

# Necessary to prevent import issues on APRSInterface
import sys
sys.path.append("./aprs_decoding/test")

from APRSInterface import APRSInterface

# these are the GPIO pins we are controlling the relay switch with
ANTENNA_1_PIN = 17
ANTENNA_2_PIN = 27

def main():
    aprs_interface = APRSInterface()

    sensor = BNOInterface()

    # setup board
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # set output pins to output
    GPIO.setup(ANTENNA_1_PIN, GPIO.OUT)
    GPIO.setup(ANTENNA_2_PIN, GPIO.OUT)

    choose_antenna(sensor)

    aprs_interface.startRecv()

    try:
        while True:
            choose_antenna(sensor)
    except KeyboardInterrupt:
        pass

    aprs_interface.stop()

def choose_antenna(sensor: BNOInterface):

    #setup orientation determination

    gravity = sensor.get_gravity()
    print(f'Gravity: {gravity}')

    # antenna 1 , IMU UP or IMU rotated 90 degrees CCW from up position
    # (looking at the bulkhead from the aft posiiton)

    # choose antenna 2
    if gravity[2] > 8.5 or gravity[1] < -8.5:
        # set output pins to output
        GPIO.setup(ANTENNA_1_PIN, GPIO.OUT)
        GPIO.setup(ANTENNA_2_PIN, GPIO.OUT)
        GPIO.output(ANTENNA_1_PIN, True)
        GPIO.output(ANTENNA_2_PIN, False)

        print("Chose antenna 2")

    # choose antenna 1
    elif gravity[2] < -8.5 or gravity[1] < 8.5:
        # set output pins to output
        GPIO.setup(ANTENNA_1_PIN, GPIO.OUT)
        GPIO.setup(ANTENNA_2_PIN, GPIO.OUT)
        GPIO.output(ANTENNA_2_PIN, True)
        GPIO.output(ANTENNA_1_PIN, False)

        print("Chose antenna 1")
    else:
        GPIO.setup(ANTENNA_1_PIN, GPIO.OUT)
        GPIO.setup(ANTENNA_2_PIN, GPIO.OUT)
        GPIO.output(ANTENNA_2_PIN, True)
        GPIO.output(ANTENNA_1_PIN, False)

        print(f"Error reading gravity data: {gravity}")
        print("Chose antenna 1")

if __name__ == "__main__":
    main()
