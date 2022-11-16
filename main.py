import RPi.GPIO as GPIO
import BNOInterface
import APRSInterface from APRSInterface

def main():
    aprsInterface = APRSInterface()

    chooseAntenna()

    aprsInterface.startRecv()

    while True:
        try:
            pass

        except KeyboardInterrupt:
            break

    aprsInterface.stop()

def chooseAntenna():
    sensor = BNOInterface.BNOInterface()
    antenna_1_pin = 11
    antenna_2_pin = 13

    # setup board
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # set output pins to output
    GPIO.setup(antenna_1_pin, GPIO.OUT)
    GPIO.setup(antenna_2_pin, GPIO.OUT)

    #setup orientation determination
    angle = 0
    angle = sensor.get_euler()[2] #using the z-axis euler angle to determine orientation

    if angle in range(0, 135) or angle in range (315, 360):
        GPIO.output(antenna_2_pin, True)
        GPIO.output(antenna_1_pin, False)
    elif angle in range(135, 315):
        GPIO.output(antenna_1_pin, True)
        GPIO.output(antenna_2_pin, False)

if __name__ == "__main__":
    main()
