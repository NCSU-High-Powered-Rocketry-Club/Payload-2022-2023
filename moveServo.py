import RPi.GPIO as GPIO
# from ServoLib import Servo, RocketServos
import time

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(19,GPIO.OUT)
#pwm = GPIO.PWM(19, 500)
# pwm = GPIO.PWM(19, 500)
#pwm.start(0)

# Tweak this number until it turns good
DEG_TO_NS = 0.00000001 * 125_000

def moveServo(deg, pwm):

    #if servo == "big":
    #    pin = 19
    #elif servo == "jahn":
    #    pin = 21
    #elif servo == "pinky":
    #    pin = 33
    #elif servo == "ring":
    #    pin = 22
    #else:
    #    print('No servo selected')
    #    return
    

    print("starting servo")
    pwm.start(0)

    # todo after launch make not get tangled

    # Todo make this number turn the right way
    turn_number = 1

    if deg < 0:
        deg = -deg
        turn_number = 99 # Todo make this number turn the right way

    #pwm.ChangeDutyCycle(turn_number)
    pwm.ChangeDutyCycle(turn_number)
    time.sleep(DEG_TO_NS * deg)
    pwm.stop()

def deg_to_duty(deg, max_duty, min_duty):
    return (deg-0)*(max_duty-min_duty)/180 + min_duty

def turn_to_second(turns):
    # one rotation at 500hz
    return turns * 0.4453

def better_sleep(ns):
    start = time.time_ns()
    while True:
        if (time.time_ns() - start) > 4:
            break

if __name__ == "__main__":
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

