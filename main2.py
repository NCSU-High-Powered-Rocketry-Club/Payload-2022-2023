import SOCS
import RPi.GPIO as GPIO

# Command line arguments
import argparse

# Necessary to prevent import issues on APRSInterface
import sys
sys.path.append("./aprs_decoding/test")

# APRS Interface
if True:
    from APRSInterface import APRSInterface


msg = "Main HPRC Payload Program."

# Initialize parser
parser = argparse.ArgumentParser(description=msg)
# Adding APRS frequency argument
parser.add_argument("-f", "--Frequency", help="APRS Frequency in MHz")
args = parser.parse_args()


def main(args):
    if args.Frequency:
        payload = SOCS.PayloadSystem(frequency=args.Frequency)
    else:
        payload = SOCS.PayloadSystem()

    try:
        while payload.state is not payload.LaunchState.RECOVER:
            payload.update()

    except KeyboardInterrupt:
        if payload.aprs_interface.running:
            payload.aprs_interface.stop()
        pass

    print("Program complete. Waiting for recovery.")


if __name__ == "__main__":
    main(args)
