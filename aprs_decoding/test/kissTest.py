import aprs
import kiss
import aprspy
#from pykiss import kiss as pk
#import pkgutil
#import kiss3
#import kiss    
import binascii
import struct
import sys, subprocess
import threading

def p(x): 
    try:
        print(x)
        data = x#str(x)
        newFrame = aprs.parse_frame(data)
        print(str(newFrame))
        packet = aprspy.APRS.parse(str(newFrame))
        print(packet)
        print(packet.source)
        print(packet.destination)
        print(packet.path)
        print(packet.timestamp)
        print(packet.info)
        
        if str(packet).startswith("<MessagePacket"):
            print(packet.message)
        
    except:
        print("failed to parse message lmao")
    #print(aprspy.APRS.parse(x).info)
    
def startWavFile(potato):
    command = 'sox -t wav ISSpkt_full.wav -esigned-integer -b 16 -r 48000 -t raw - | direwolf -B 1200 -c direwolf.conf -b 16 -n 1 -r 48000 -a 0 -'
    proc = subprocess.call(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    
def main():
    newThread = threading.Thread(target= startWavFile, args=(2,))
    newThread.start()
    ki = kiss.TCPKISS(host='localhost', port=8001)
    ki.start()
    while True:
        
        ki.read(callback=p)
        
    newThread.join()
    

if __name__ == '__main__':
    main()
    
