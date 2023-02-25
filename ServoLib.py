import RPi.GPIO as GPIO
from enum import Enum
import time

class Servo:
    def __init__(self, servoPin, uSPerDeg):
        self.servoPin = servoPin
        GPIO.setwarnings(False)			#disable warnings
        GPIO.setmode(GPIO.BOARD)		#set pin numbering system

        print (f"Initialzing servo on pin {self.servoPin}")

        # set the servo pin to output
        GPIO.setup(self.servoPin, GPIO.OUT)

        #create PWM instance with frequency
        self.pi_pwm = GPIO.PWM(self.servoPin, 100)

        # start PWM of required Duty Cycle
        self.pi_pwm.start(15) 

        self.nsPerDeg = uSPerDeg
        self.currentAngle = 0

    def set_degrees(self, deg):
        print(f"Set servo angle {deg}")
        print(f"Microseconds: {deg * self.nsPerDeg}")

        dutyCycle = 1 if deg < 0 else 30 # might need to reverse

        start = time.time_ns()
        end = start + abs(deg) * self.nsPerDeg

        print(f"Duration: {end - start}ns, duty cycle: {dutyCycle}")

        self.pi_pwm.ChangeDutyCycle(dutyCycle)
        while time.time_ns() < end:
            # print(f"Start: {start} | End: {end}")
            pass
        print("done!")
        self.pi_pwm.ChangeDutyCycle(15)
        # self.currentAngle = deg
        
class RocketServos(Enum):
    BIG = Servo(19, 1000)
    JAHN = Servo(21, 909090+10000)
    RING = Servo(22, 1000)
    PINKY = Servo(23, 1000)
