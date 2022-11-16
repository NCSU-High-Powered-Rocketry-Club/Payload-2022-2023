import aprs
import kiss
import aprspy
import sys, subprocess
import threading
import time

def p(x): 
    try:
        print("\n----New data----")
        print("Raw data from KISS: "+str(x))
        data = x
        
        newFrame = aprs.parse_frame(data)
        
        print("Parsed APRS frame: "+ str(newFrame))
        
        packet = aprspy.APRS.parse(str(newFrame))
        
        print("APRS Packet: "+ str(packet))
        print("Source: "+ str(packet.source))
        print("Destination: "+ str(packet.destination))
        print("Path: "+ str(packet.path))
        print("Timestamp: "+ str(packet.timestamp))
        print("Info: "+ str(packet.info))
        
        if str(packet).startswith("<MessagePacket"):
            print("Message: "+ str(packet.message))
        
    except:
        print("failed to parse message lmao (not a MessagePacket)")


def startWavFile(potato):
    command = 'rtl_fm -f 445.15M -s 48000 -o 4 - | direwolf -B 1200 -c direwolf.conf -b 16 -n 1 -r 48000 -a 0 -'
    proc = subprocess.call(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    
def main():
    newThread = threading.Thread(target= startWavFile, args=(2,))
    newThread.start()
    time.sleep(0.8)
    ki = kiss.TCPKISS(host='localhost', port=8001)
    ki.start()
    
    while True:#(not keyboard.is_pressed('q')):
        ki.read(callback=p)
    
    print("Exiting...")
    newThread.join()
    ki.stop()
    

if __name__ == '__main__':
    main()
    
