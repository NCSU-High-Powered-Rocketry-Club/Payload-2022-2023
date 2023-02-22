import RPi.GPIO as gp
import os

gp.setwarnings(False)

gp.setup(15, gp.OUT)
gp.setup(16, gp.OUT)
gp.setup(18, gp.OUT)

def takepic(topcam, x):
    if topcam == "big":
        print('Big Toe')
        i2c = "i2cset -y 1 0x70 0x00 0x04" # i2c for camera A (big toe)
        os.system(i2c)
        gp.output(15, False)
        gp.output(16, False)
        gp.output(18, True)
        capture(topcam, x)
    elif topcam == "pinky":
        print('Pinky Toe') 
        i2c = "i2cset -y 1 0x70 0x00 0x05"
        os.system(i2c)
        gp.output(15, True)
        gp.output(16, False)
        gp.output(18, True)
        capture(topcam, x)
    elif topcam == "ring":
        print("Ring Toe")
        i2c = "i2cset -y 1 0x70 0x00 0x06"
        os.system(i2c)
        gp.output(15, False)
        gp.output(16, True)
        gp.output(18, False)
        capture(topcam, x)
    elif topcam == "jahn":
        print("Jahn")
        i2c = "i2cset -y 1 0x70 0x00 0x07"
        os.system(i2c)
        gp.output(15, True)
        gp.output(16, True)
        gp.output(18, False)
        capture(topcam, x)
    else:
        print("uh oh")
    
def capture(cam,x):
    cmd = "libcamera-still -o capture_%s_%d.jpg" % (cam, x)
    os.system(cmd)