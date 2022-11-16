import aprs
import kiss
import aprspy
import sys, subprocess
import threading
import time

class APRSInterface:
    def __init__():
        pass

    def stop():
        self.running = False

        self.recvThread.join()
        self.kissThread.join()

    def startRecv(self):
        self.running = True

        self.recvThread = threading.Thread(target=direwolfRecvThread)
        self.recvThread.start()

        time.sleep(0.8)

        self.kissThread = threading.Thread(target=kissParseThread)
        self.kissThread.start()

    def direwolfRecvThread(self):
        command = 'rtl_fm -f 445.15M -s 48000 -o 4 - | direwolf -B 1200 -c direwolf.conf -b 16 -n 1 -r 48000 -a 0 -'
        proc = subprocess.call(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    def kissParseThread(self):
        self.ki = kiss.TCPKISS(host='localhost', port=8001)
        self.ki.start()

        while self.running:
            ki.read(callback=printPacket)

        ki.stop()

    def printPacket(packet):
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
            