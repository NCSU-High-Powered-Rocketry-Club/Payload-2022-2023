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

<<<<<<< HEAD
        print("Starting direwolf thread")
        self.recvThread = threading.Thread(target=self.direwolfRecvThread)
=======
        # Start Direwolf TNC and rtl_fm
        self.recvThread = threading.Thread(target=direwolfRecvThread)
>>>>>>> a881817cd8a0a6e2d720be4b440e364f77cd6400
        self.recvThread.start()

        # Wait for TCP socket to start up 
        # (current value is just a rough estimate)
        time.sleep(0.8)

<<<<<<< HEAD
        print("Starting kiss thread")
        self.kissThread = threading.Thread(target=self.kissParseThread)
=======
        # Start data parsing thread
        self.kissThread = threading.Thread(target=kissParseThread)
>>>>>>> a881817cd8a0a6e2d720be4b440e364f77cd6400
        self.kissThread.start()

    def direwolfRecvThread(self):
    
        # Command to start rtl_fm to read data from RTL-SDR dongle and pipe it to direwolf.
        
        # Use sox -t wav ISSpkt_full.wav -esigned-integer -b 16 -r 48000 -t raw - |
        # to read from .wav file named ISSpkt_full.wav
        
        # And use rtl_fm -f 445.15M -s 48000 -o 4 - |
        # to read from the RTL-SDR, where 445.15 is the center frequency in MHz
        
        command = 'rtl_fm -f 445.15M -s 48000 -o 4 - | direwolf -B 1200 -c direwolf.conf -b 16 -n 1 -r 48000 -a 0 -'
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

        while self.running:
            pass

        proc.terminate()

    def kissParseThread(self):
    
        # Start KISS TCP listener
        self.ki = kiss.TCPKISS(host='localhost', port=8001)
        self.ki.start()

        # Continuously look for and print packets
        while self.running:
           self.ki.read(callback=self.printPacket)

        # Stop when done
        ki.stop()

    def printPacket(raw_data):
        try:
            print("\n----New data----")
            print("Raw data from KISS: "+str(raw_data))
            
            # Turn raw input bytes from KISS into an APRS frame
            newFrame = aprs.parse_frame(raw_data)
            
            print("Parsed APRS frame: "+ str(newFrame))
            
            # Turn the APRS frame into an aprspy library APRS object because
            # only aprspy has actual documentation on reading the data 
            packet = aprspy.APRS.parse(str(newFrame))
            
            # Print data common to all packet types
            print("APRS Packet: "+ str(packet))
            print("Source: "+ str(packet.source))
            print("Destination: "+ str(packet.destination))
            print("Path: "+ str(packet.path))
            print("Timestamp: "+ str(packet.timestamp))
            print("Info: "+ str(packet.info))
            
            # Print message if this is a message packet
            # (there may be a better way to check packet type, but this works)
            if str(packet).startswith("<MessagePacket"):
                print("Message: "+ str(packet.message))
            
        except:
            # Sometimes you just get bad data cuz the signal is wonky
            print("failed to parse message lmao")
            
