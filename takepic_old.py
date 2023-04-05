import RPi.GPIO as GPIO
import os

#gp.cleanup()

#gp.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

def takepic(topcam, x):
    if topcam == "jahn": # Camera A
        print('Jahn Toe')
        i2c = "i2cset -y 1 0x70 0x00 0x04" # i2c for camera A (big toe)
        os.system(i2c)
        GPIO.output(15, False)
        GPIO.output(16, False)
        GPIO.output(18, True)
        capture(topcam, x)
    elif topcam == "big": # Camera B
        print('Big Toe') 
        i2c = "i2cset -y 1 0x70 0x00 0x05" # Camera B (Pinky)
        os.system(i2c)
        GPIO.output(15, True)
        GPIO.output(16, False)
        GPIO.output(18, True)
        capture(topcam, x)
    elif topcam == "ring": # Camera C
        print("Ring Toe")
        i2c = "i2cset -y 1 0x70 0x00 0x06" # Camera C (Ring)
        os.system(i2c)
        GPIO.output(15, False)
        GPIO.output(16, True)
        GPIO.output(18, False)
        capture(topcam, x)
    elif topcam == "pinky": # Camera D
        print("Pinky Toe")
        i2c = "i2cset -y 1 0x70 0x00 0x07" # Camera D (Jahn)
        os.system(i2c)
        GPIO.output(15, True)
        GPIO.output(16, True)
        GPIO.output(18, False)
        capture(topcam, x)
    else:
        print("uh oh")
    
def capture(cam,x):
    cmd = "libcamera-still -n -o capture_%s_%d.jpg" % (cam, x)
    os.system(cmd)

if __name__ == "__main__":
    takepic("big", 0)
    takepic("pinky", 0)
    takepic("ring", 0)
    takepic("jahn", 0)
