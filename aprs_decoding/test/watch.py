# watch_aprs.py
# A simple Python script by G7UHN to do stuff when given text is received by a RTL/BeagleBone APRS receiver

import sys, subprocess
#import PIPE

# Guidance from https://stackoverflow.com/questions/2804543/read-subprocess-stdout-line-by-line

proc = subprocess.Popen('rtl_fm -f 144.80M - | direwolf -c sdr.conf -r 24000 -t 0 -D 1 -', stdout=subprocess.PIPE, shell=True)

while True:
    line = proc.stdout.readline()
    if line != '':
        print ("Decoded:", line.rstrip())
        if "G7UHN" in str(line): 
            print("Look it's my call!! :-) ")
    else: 
        break