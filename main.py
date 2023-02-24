import RPi.GPIO as GPIO
from enum import Enum
from BNOInterface import BNOInterface
import time
from PIL import Image
import executeCmdsPDF # Change for Hville

# Necessary to prevent import issues on APRSInterface
import sys
sys.path.append("./aprs_decoding/test")

from APRSInterface import APRSInterface

#Command line arguments
import argparse

msg = "Main HPRC Payload Program." 

# Initialize parser
parser = argparse.ArgumentParser(description=msg)
# Adding APRS frequency argument
parser.add_argument("-f", "--Frequency", help = "APRS Frequency in MHz")
args = parser.parse_args()


# rocket state
class State(Enum):
    STANDBY = 0
    LAUNCH = 1
    LANDING = 2

# time from launch to landing, in seconds
DESCENT_TIME = 10

# amount of values to collect for rolling launch detect average
AVERAGE_COUNT = 250

# these are the GPIO pins we are controlling the relay switch with
ANTENNA_1_PIN = 17
ANTENNA_2_PIN = 27

def main(args):
    if args.Frequency:
        aprs_interface = APRSInterface(frequency=args.Frequency)
    else:
        aprs_interface = APRSInterface()

    sensor = BNOInterface()

    state = State.STANDBY

    # setup board
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # set output pins to output
    GPIO.setup(ANTENNA_1_PIN, GPIO.OUT)
    GPIO.setup(ANTENNA_2_PIN, GPIO.OUT)

    # launch detection
    accelerations = [0] * AVERAGE_COUNT
    idx = 0

    while state is State.STANDBY:
        accel = sensor.get_linear_acceleration()
        # print(accel)
        if accel != (None, None, None):
            accelerations[idx] = abs(accel[0])

            idx = (idx+1) % AVERAGE_COUNT

            average_accel = sum(accelerations) / AVERAGE_COUNT
            # print(average_accel)

            if average_accel > 3:
                state = State.LAUNCH

    print("LIFTOFF DETECTED")

    # delay for descent time
    delayStart = time.time()
    while state is State.LAUNCH:
        if delayStart + DESCENT_TIME < time.time():
            state = State.LANDING

    print("LANDED! Choosing antenna...")

    choose_antenna(sensor)

    aprs_interface.startRecv()

    try:
        while True:
            choose_antenna(sensor)
            cam_choice = choose_antenna(sensor)
            if len(aprs_interface.aprsMsg) > 0:
                break
    except KeyboardInterrupt:
        pass

    aprs_interface.stop()
    print("%s" % aprs_interface.aprsMsg[0][7:])

    # Need to check that the callsign is actually from NASA; must add that here
    # The index of 7 takes out the callsign
    # Execute the commands for the camera unit
    APRS_clip = aprs_interface.aprsMsg[0][7:]
    executeCmdsPDF.executeCmdsPDF(APRS_clip, cam_choice) # Change to executeCmds for Hville


def choose_antenna(sensor: BNOInterface):

    #setup orientation determination

    gravity = sensor.get_gravity()
    print(f'Gravity: {gravity}')

    # antenna 1 , IMU UP or IMU rotated 90 degrees CCW from up position
    # (looking at the bulkhead from the aft posiiton)
    # skip none type gravity
    try:
        gravity[2] > 0
    except:
        return

    # choose antenna 2
    if gravity[2] > 8.5*0.707 or gravity[1] < -8.5*0.707:
        # set output pins to output
        GPIO.output(ANTENNA_1_PIN, True)
        GPIO.output(ANTENNA_2_PIN, False)

        if gravity[1] < -1 and gravity[2] < -1:
            cam_choice = "big"
            #print("big")
        else: #gravity[1] > 1 and gravity[2] < -1:
            cam_choice = "jahn"
            #print("jahn")
        # print("Chose antenna 2")

    # choose antenna 1
    elif gravity[2] < -8.5*0.707 or gravity[1] < 8.5*0.707:
        # set output pins to output
        GPIO.output(ANTENNA_2_PIN, True)
        GPIO.output(ANTENNA_1_PIN, False)
        # print("Chose antenna 1")

        if gravity[1] > 1 and gravity[2] > 1:
            cam_choice = "pinky"
            #print("pinky")
        else: #gravity[1] < -1 and gravity[2] > 1:
            cam_choice = "ring"
            #print("pinky")

    else:
        GPIO.output(ANTENNA_2_PIN, True)
        GPIO.output(ANTENNA_1_PIN, False)

        cam_choice = "big"
        #print("No camera chosen")

        # print(f"Error reading gravity data: {gravity}")
        # print("Chose antenna 1")
    return cam_choice

if __name__ == "__main__":
    main(args)