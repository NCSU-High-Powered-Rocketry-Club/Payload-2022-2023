import RPi.GPIO as GPIO
from Servo import Servo
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19,GPIO.OUT)
pwm = GPIO.PWM(19, 500)
# pwm = GPIO.PWM(19, 500)
pwm.start(0)

def moveServo(deg, servo):
    GPIO.setmode(GPIO.BOARD)
    if servo == "big":
        GPIO.setup(19,GPIO.OUT)
        pwm = GPIO.PWM(19, 500)
        pwm.start(0)
        pwm.ChangeDutyCycle(deg)
        time.sleep(1)
        pwm.stop()
    elif servo == "jahn":
        GPIO.setup(21,GPIO.OUT)
        pwm = GPIO.PWM(21, 500)
        pwm.start(0)
        pwm.ChangeDutyCycle(deg)
        time.sleep(1)
        pwm.stop()
    elif servo == "pinky":
        GPIO.setup(23,GPIO.OUT)
        pwm = GPIO.PWM(23, 500)
        pwm.start(0)
        pwm.ChangeDutyCycle(deg)
        time.sleep(1)
        pwm.stop()
    elif servo == "ring":
        GPIO.setup(22,GPIO.OUT)
        pwm = GPIO.PWM(22, 500)
        pwm.start(0)
        pwm.ChangeDutyCycle(deg)
        time.sleep(1)
        pwm.stop()
    else:
        print('No servo selected')
    print('0')
    pwm.ChangeDutyCycle(10)
    time.sleep(1)
    print('0.5')
    pwm.ChangeDutyCycle(50)
    time.sleep(1)
    print('1')
    pwm.ChangeDutyCycle(90)
    time.sleep(1)

def turn_to_second(turns):
    # return turns * 0.4453 # one rotation at 500hz
    return turns * 0.4453

while True:
    # pwm.ChangeDutyCycle(int(input()))
    # s = turn_to_second(int(input()))
    # pwm.ChangeDutyCycle(10)
    # time.sleep(s)
    # pwm.ChangeDutyCycle(0)
    # testServo()

    # Stress test
    if True:
        s = turn_to_second(1) * 1_000_000_000
        # s = 1 * 1_000_000_000
        pwm.ChangeDutyCycle(10)
        start = time.time_ns()
        while True:
            if (time.time_ns() - start) > s:
                break
        pwm.ChangeDutyCycle(0)
        time.sleep(0.5)

        pwm.ChangeDutyCycle(90)
        start = time.time_ns()
        while True:
            if (time.time_ns() - start) > s:
                break
        pwm.ChangeDutyCycle(0)
        time.sleep(0.5)

    # 40 turns in 20.82 seconds

