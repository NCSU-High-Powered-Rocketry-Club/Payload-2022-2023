import RPi.GPIO as gp
import os

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(15, gp.OUT)
gp.setup(16, gp.OUT)
gp.setup(18, gp.OUT)


def main():
    print('Start testing the camera A')
    i2c = "i2cset -y 0 0x70 0x00 0x04"
    os.system(i2c)
    gp.output(15, False)
    gp.output(16, False)
    gp.output(18, True)
    capture(1)
    print('Start testing the camera B') 
    i2c = "i2cset -y 0 0x70 0x00 0x05"
    os.system(i2c)
    gp.output(15, True)
    gp.output(16, False)
    gp.output(18, True)
    capture(2)
    print('Start testing the camera C')
    i2c = "i2cset -y 0 0x70 0x00 0x06"
    os.system(i2c)
    gp.output(15, False)
    gp.output(16, True)
    gp.output(18, False)
    capture(3)
    print('Start testing the camera D')
    i2c = "i2cset -y 0 0x70 0x00 0x07"
    os.system(i2c)
    gp.output(15, True)
    gp.output(16, True)
    gp.output(18, False)
    capture(4)
    
def capture(cam):
    cmd = "libcamera-still -n -o capture_%d.jpg" % cam
    os.system(cmd)

if __name__ == "__main__":
    main()

    gp.output(15, False)
    gp.output(16, False)
    gp.output(18, True)
