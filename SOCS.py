import argparse
import RPi.GPIO as GPIO
from enum import Enum
from BNOInterface import BNOInterface
import time
from PIL import Image
import executeCmds  # Change for Hville
import asyncio
import mathutils

# Necessary to prevent import issues on APRSInterface
import sys
sys.path.append("./aprs_decoding/test")

# APRS Interface
if True:
    from APRSInterface import APRSInterface


class PayloadSystem:

    # time from launch to landing, in seconds
    DESCENT_TIME = 10

    # amount of values to collect for rolling launch detect average
    AVERAGE_COUNT = 250

    # these are the GPIO pins we are controlling the relay switch with
    ANTENNA_1_PIN = 17
    ANTENNA_2_PIN = 27

    # rocket state
    class LaunchState(Enum):
        STANDBY = 0
        LAUNCH = 1
        LANDING = 2
        CAMERA = 3
        RECOVER = 4

    def __init__(self, frequency=None):
        if frequency != None:
            self.aprs_interface = APRSInterface(frequency=frequency)
        else:
            self.aprs_interface = APRSInterface()

        self.sensor = BNOInterface()
        self.state = self.LaunchState.STANDBY

        # setup board
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        # set output pins to output
        GPIO.setup(self.ANTENNA_1_PIN, GPIO.OUT)
        GPIO.setup(self.ANTENNA_2_PIN, GPIO.OUT)

        # launch detection
        self.accelerations = [0] * self.AVERAGE_COUNT
        self.idx = 0

        # Variable to track whether message received
        self.messageReceived = False

    def update(self):
        currentState = self.state
        if currentState is self.LaunchState.STANDBY:
            # Do standby stuff
            accel = self.sensor.get_linear_acceleration()
            print(accel)
            if accel != (None, None, None):
                self.accelerations[idx] = abs(accel[0])

                idx = (idx+1) % self.AVERAGE_COUNT

                average_accel = sum(self.accelerations) / self.AVERAGE_COUNT
                # print(average_accel)

                if average_accel > 3:
                    self.delayStart = time.time()
                    self.state = self.LaunchState.LAUNCH
                    print("LIFTOFF DETECTED")

        elif currentState is self.LaunchState.LAUNCH:
            # Do launch stuff
            # Need to check and make sure it's landed
            if time.time() > (self.delayStart + self.DESCENT_TIME):
                # This will also be done continuously in landed state so idk
                self.choose_antenna(self)
                self.aprs_interface.startRecv()

                self.state = self.LaunchState.LANDING
                print("LANDED! Choosing antenna...")

        elif currentState is self.LaunchState.LANDING:
            # Do landing stuff

            self.choose_antenna(self)

            print("Number of messages: " + str(len(self.aprs_interface.aprsMsg)))

            # Need to check that the callsign is actually from NASA; must add that here
            if len(self.aprs_interface.aprsMsg) > 0:
                self.aprs_interface.stop()
                self.messageReceived = True
                self.state = self.LaunchState.CAMERA

        elif currentState is self.LaunchState.CAMERA:

            self.cameraChoice = self.choose_antennachoose_antenna

            print(f"Full Message: {self.aprs_interface.aprsMsg[0]}")

            # The index of 7 takes out the callsign
            print(f"Sliced Message: {self.aprs_interface.aprsMsg[0][7:]}")

            # The index of 7 takes out the callsign
            APRS_clip = self.aprs_interface.aprsMsg[0][7:]
            # Change to executeCmds for Hville
            # Execute the commands for the camera unit
            asyncio.run(executeCmds.executeCmds(APRS_clip, cam))

            self.state = self.LaunchState.RECOVER

    def choose_antenna(self):

        # setup orientation determination

        gravity = self.sensor.get_gravity()
        # print(f'Gravity: {gravity}')

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
            GPIO.output(self.ANTENNA_1_PIN, True)
            GPIO.output(self.ANTENNA_2_PIN, False)

            if gravity[1] < -1 and gravity[2] < -1:
                cam_choice = "big"
                print("big")
            else: #gravity[1] > 1 and gravity[2] < -1
                cam_choice = "jahn"
                print("jahn")
            print("Chose antenna 2")

        # choose antenna 1
        elif gravity[2] < -8.5*0.707 or gravity[1] < 8.5*0.707:
            # set output pins to output
            GPIO.output(self.ANTENNA_2_PIN, True)
            GPIO.output(self.ANTENNA_1_PIN, False)

            if gravity[1] > 1 and gravity[2] > 1:
                cam_choice = "pinky"
                print("pinky")
            else: #gravity[1] < -1 and gravity[2] > 1:cam_choice = "ring"
                cam_choice = "ring"
                print("ring")

            print("Chose antenna 1")

        else:
            GPIO.output(self.ANTENNA_2_PIN, True)
            GPIO.output(self.ANTENNA_1_PIN, False)

            cam_choice = "big"
            print("No camera chosen")

            print(f"Error reading gravity data: {gravity}")
            print("Chose antenna 1")
        return cam_choice
