import aprs_decoding.test.aprs as aprs
import aprs_decoding.test.kiss as kiss
import aprspy
import subprocess
import threading
import time
import logging


class APRSInterface:
    def __init__(self, frequency: str = "144.39"):
        # Set the logfile config and formatting
        # Make the logger print to stderr as well as log to file
        logging.basicConfig(handlers=[
            logging.FileHandler("APRS_log.txt"),
            logging.StreamHandler()
        ], level=logging.DEBUG,
            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.aprsMsg = []
        self.frequency = frequency

    def stop(self):
        self.running = False

        print("shutting down...")

        self.recvThread.join()
        print("Direwolf thread shutdown")
        self.kissThread.join()
        print("Kiss thread shutdown")

    def startRecv(self):
        self.running = True

        # Start Direwolf TNC and rtl_fm
        print("Starting direwolf thread")
        self.recvThread = threading.Thread(target=self.direwolfRecvThread)

        self.recvThread.start()

        # Wait for TCP socket to start up
        # (current value is just a rough estimate)
        time.sleep(0.8)

        # Start data parsing thread
        print("Starting kiss thread")
        self.kissThread = threading.Thread(target=self.kissParseThread)

        self.kissThread.start()

    def direwolfRecvThread(self):

        # Command to start rtl_fm to read data from RTL-SDR dongle and pipe it to direwolf.

        # Use sox -t wav ISSpkt_full.wav -esigned-integer -b 16 -r 48000 -t raw - |
        # to read from .wav file named ISSpkt_full.wav

        # And use rtl_fm -f 445.15M -s 48000 -o 4 - |
        # to read from the RTL-SDR, where 445.15 is the center frequency in MHz

        command = f'rtl_fm -f {self.frequency}M -s 48000 -o 4 - | direwolf -B 1200 -c direwolf.conf -b 16 -n 1 -r 48000 -a 0 -'

        proc = subprocess.Popen(
            command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

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
        self.ki.stop()

    def printPacket(self, raw_data):

        logMsgs = []
        logMsgs.append("----New data----")
        logMsgs.append("Raw data from KISS: "+str(raw_data))
        logging.debug("\n".join(logMsgs))

        logMsgs = []
        # Turn raw input bytes from KISS into an APRS frame
        newFrame = aprs.parse_frame(raw_data)
        newFrame = str(newFrame).replace("-6",'')

        logMsgs.append("Parsed APRS frame: " + str(newFrame))
        logging.debug("\n".join(logMsgs))

        logMsgs = []
        # Turn the APRS frame into an aprspy library APRS object because
        # only aprspy has actual documentation on reading the data
        packet = aprspy.APRS.parse(str(newFrame), strict_mode=False)

        # Print data common to all packet types
        logMsgs.append(f"APRS Packet: {str(packet)}")
        logMsgs.append(f"Source: {str(packet.source)}")
        logMsgs.append(f"Destination: {str(packet.destination)}")
        logMsgs.append(f"Path: {str(packet.path)}")
        logMsgs.append(f"Timestamp: {str(packet.timestamp)}")
        logMsgs.append(f"Info: {str(packet.info)}")

        # Print message if this is a message packet
        # (there may be a better way to check packet type, but this works)
        # Create a global variable aprsMsg that can be used to execute cmds
        if str(packet).startswith("<MIC-E"):
            logMsgs.append("Message: " + str(packet.message))
            self.aprsMsg.append(str(packet.message))

        # Join all the messages together and log it as one debug message
        logging.debug("\n".join(logMsgs))

        # Sometimes you just get bad data cuz the signal is wonky
        # logging.debug("failed to parse message lmao")
