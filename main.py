import APRSDecoder.py
import BNOInterface.py

def main():

    angle = 0

    if angle in range(0, 45):
        orientation = 0
    elif angle in range(45, 135):
        orientation = 1
    elif angle in range(135, 225):
        orientation = 2
    elif angle in range(225, 315):
        orientation = 3
    elif: angle in range(315, 360):
        orientation = 0



if __name__ == "__main__":
    main()
