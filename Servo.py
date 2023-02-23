import RPi.GPIO as GPIO
from enum import Enum
import time

class Servo:
    def __init__(self, servoPin, uSPerDeg):
        self.servoPin = servoPin
        GPIO.setwarnings(False)			#disable warnings
        GPIO.setmode(GPIO.BOARD)		#set pin numbering system

        # set the servo pin to output
        GPIO.setup(self.servoPin, GPIO.OUT)

        #create PWM instance with frequency
        self.pi_pwm = GPIO.PWM(self.servoPin, 50)

        # start PWM of required Duty Cycle
        self.pi_pwm.start(500) 

        self.uSPerDeg = uSPerDeg
        self.currentAngle = 0

    def set_degrees(self, deg):
        print(f"Set servo angle {deg}")
        print(f"Microseconds: {deg * self.uSPerDeg}")

        dutyCycle = 0 if deg > self.currentAngle else 1000 # might need to reverse

        self.pi_pwm.ChangeDutyCycle(dutyCycle)
        time.sleep(self.uSPerDeg * deg)
        self.pi_pwm.ChangeDutyCycle(500)
        
class RocketServos(Enum):
    BIG = Servo(19, 1000)
    JAHN = Servo(21, 1000)
    RING = Servo(22, 1000)
    PINKY = Servo(33, 1000)
