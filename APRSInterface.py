import aprs_decoding.test.aprs as aprs
import aprs_decoding.test.kiss as kiss
import aprspy
import subprocess
import threading
import time

class APRSInterface:
    def __init__(self):
        pass

    def stop(self):
        self.running = False

        print("shutting down...")

        self.recvThread.join()
        print("Direwolf thread shutdown")
        self.kissThread.join()
        print("Kiss thread shutdown")

    def startRecv(self):
        self.running = True

        print("Starting direwolf thread")
        self.recvThread = threading.Thread(target=self.direwolfRecvThread)
        self.recvThread.start()

        time.sleep(0.8)

        print("Starting kiss thread")
        self.kissThread = threading.Thread(target=self.kissParseThread)
        self.kissThread.start()

    def direwolfRecvThread(self):
        command = 'rtl_fm -f 445.15M -s 48000 -o 4 - | direwolf -B 1200 -c direwolf.conf -b 16 -n 1 -r 48000 -a 0 -'
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

        while self.running:
            pass

        proc.terminate()

    def kissParseThread(self):
        self.ki = kiss.TCPKISS(host='localhost', port=8001)
        self.ki.start()

        while self.running:
           self.ki.read(callback=self.printPacket)

        self.ki.stop()

    def printPacket(packet):
        try:
            print("\n----New data----")
            print("Raw data from KISS: "+str(packet))
            
            newFrame = aprs.parse_frame(packet)
            
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
            