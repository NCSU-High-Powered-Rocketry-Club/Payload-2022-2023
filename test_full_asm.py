import RPi.GPIO as GPIO
from Servo import RocketServos, Servo
import time

def main():
    print("""
        Servos:
        1. Big
        2. Jahn
        3. Ring
        4. Pinky
    """)
    servo_num = input("Which servo would you like to test? ")
    servo: Servo = RocketServos(int(servo_num-1)).value

    print("Rotating -30 deg")
    servo.set_degrees(-30)
    
    print("Waiting 3 seconds, then rotating +60 deg")
    time.sleep(3)
    servo.set_degrees(30)

    print("Waiting 3 seconds, then rotating -30 deg (back to 0)")
    time.sleep(3)
    servo.set_degrees(0)


if __name__ == "__main__":
    main()