import RPi.GPIO as GPIO
from enum import Enum
from BNOInterface import BNOInterface
import time
from PIL import Image
import executeCmds

# Necessary to prevent import issues on APRSInterface
import sys
sys.path.append("./aprs_decoding/test")

from APRSInterface import APRSInterface

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

# these are the commands to select each camera
CAMERA_A = [0, 0, 1]
CAMERA_B = [1, 0, 1]
CAMERA_C = [0, 1, 0]
CAMERA_D = [1, 1, 0]

def main():
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
            if len(aprs_interface.aprsMsg) > 0:
                break
    except KeyboardInterrupt:
        pass

    aprs_interface.stop()

    # Need to check that the callsign is actually from NASA; must add that here
    # The index of 7 takes out the callsign
    # Execute the commands for the camera unit
    APRS_clip = aprs_interface.aprsMsg.pop()[7:]
    executeCmds.executeCmds(APRS_clip, camGirl)


def choose_antenna(sensor: BNOInterface):

    #setup orientation determination

    gravity = sensor.get_gravity()
    # print(f'Gravity: {gravity}')

    # antenna 1 , IMU UP or IMU rotated 90 degrees CCW from up position
    # (looking at the bulkhead from the aft posiiton)
    # skip none type gravity
    try:
        gravity[2] > 0
    except:
        return

    # choose antenna 2
    if gravity[2] > 8.5 or gravity[1] < -8.5:
        # set output pins to output
        GPIO.output(ANTENNA_1_PIN, True)
        GPIO.output(ANTENNA_2_PIN, False)

        # print("Chose antenna 2")

    # choose antenna 1
    elif gravity[2] < -8.5 or gravity[1] < 8.5:
        # set output pins to output
        GPIO.output(ANTENNA_2_PIN, True)
        GPIO.output(ANTENNA_1_PIN, False)

        # print("Chose antenna 1")
    else:
        GPIO.output(ANTENNA_2_PIN, True)
        GPIO.output(ANTENNA_1_PIN, False)

        # print(f"Error reading gravity data: {gravity}")
        # print("Chose antenna 1")

if __name__ == "__main__":
    main()

def choose_cameraUnit():
    # Choose both camera and servo
    # gravity stuff here, like above
    cameraChoice = [0, 0, 0] # This isn't an actual cam, replace w/ 1x3 array
    servoChoice = [0, 0, 0]
    return cameraChoice, servoChoice

def activate_camera(camera_number):
    # Tell the chosen camera to capture images
    camera_choice = CAMERA_C
    # send commands to camera_choice using GPIO 7, 11, 12 on Pi
    if camera_number == 1:
        # do some GPIO stuff
        return


# If RAFCO system receives command G7, choose randomly from 3 image effects (fry, grassless, and meme)
def applyfilter(): # This calls imageFilter module
    import imageFilter
    image = Image.open('pic.jpg')
    image_data = image.load()
    height,width = image.size
    imageFilter.fry(image) # This is a placeholder, replace w random number generator

#Pull out aprs msgs and pass those msgs to executeCmds.py
def execute():
    return 1

num = choose_camera()

activate_camera(num)

applyfilter()

# If RAFCO system receives command F6, rotate image 180 degrees
import imageFilter
image = imageFilter.rotate180(image)