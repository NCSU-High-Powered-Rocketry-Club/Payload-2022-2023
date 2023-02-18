import RPi.GPIO as gp
import os

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)

def takepic(topcam):
    if topcam == "big":
        print('Big Toe')
        i2c = "i2cset -y 1 0x70 0x00 0x04" # i2c for camera A (big toe)
        os.system(i2c)
        gp.output(7, False)
        gp.output(11, False)
        gp.output(12, True)
        capture(1)
    elif topcam == "pinky":
        print('Pinky Toe') 
        i2c = "i2cset -y 1 0x70 0x00 0x05"
        os.system(i2c)
        gp.output(7, True)
        gp.output(11, False)
        gp.output(12, True)
        capture(2)
    elif topcam == "ring":
        print("Ring Toe")
        i2c = "i2cset -y 1 0x70 0x00 0x06"
        os.system(i2c)
        gp.output(7, False)
        gp.output(11, True)
        gp.output(12, False)
        capture(3)
    elif topcam == "jahn":
        print("Jahn")
        i2c = "i2cset -y 1 0x70 0x00 0x07"
        os.system(i2c)
        gp.output(7, True)
        gp.output(11, True)
        gp.output(12, False)
        capture(4)
    else:
        print("uh oh")
    
def capture(cam):
    cmd = "libcamera-still -o capture_%d.jpg" % cam
    os.system(cmd)

takepic("big")
gp.output(7, False)
gp.output(11, False)
gp.output(12, True)