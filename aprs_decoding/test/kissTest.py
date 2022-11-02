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
        print(packet.message)
    except:
        print("oof")
    #print(aprspy.APRS.parse(x).info)
    

def main():
    #ki = kiss.SerialKISS(port='/dev/cu.Repleo-PL2303-00303114', speed='9600')
    #sox data.wav -c 1 -t s16 -r 48000 -t wav - | direwolf -B 1200 -c ./dire2.conf -d p -
    #proc = subprocess.run('sox data.wav -c 1 -t s16 -r 48000 -t wav - | direwolf -B 1200 -d p -')
    ki = kiss.TCPKISS(host='localhost', port=8001)
    ki.start()
    while True:
        
        ki.read(callback=p)
        
        
        

def main2():
    data = b'\x00\xa8\xa0\xa6\xaa\xa4\xac`\xae\x88n\xa0@@\xea\xae\x92\x88\x8ab@b\xae\x92\x88\x8ad@c\x03\xf0`\'U{ora>/`"Bw}_%\r'
    data2 = b'\x00\x84\x8a\x82\x86\x9e\x9c`\x98\x8e\xaa@@@`\x96\x8cl\xa4\x82\x98\xe4\xae\x92\x88\x8ad@\xe1\x03\xf0;147.260UT*111111z4117.75N/11228.09Wr147.260MHz T103 R95m Net Tu9pm Mtg2ndSA\r'
    data3 = b'\x00\x82\xa0\x9e\xa8f`\xe0\x90\x9e\x98\x88\x8a\x9c\xe0\x96\x8cl\xa4\x82\x98\xe2\xae\x92\x88\x8ad@\xe1\x03\xf0!3901.82N/11209.11W# 12.2V 25F '
    #stripped = kiss.util.strip_df_start(data)
    newFrame = aprs.parse_frame(data3)
    print(str(newFrame))
    packet = aprspy.APRS.parse(str(newFrame))
    print(packet)
    print(packet.source)
    print(packet.destination)
    print(packet.path)
    print(packet.timestamp)
    print(packet.info)
    #print(newFrame.source)
    #print(newFrame.destination)
    #print(newFrame.path)
    #print(newFrame.info)
    #print(newFrame.text)
    #for importer, modname, ispkg in pkgutil.iter_modules(aprs.__path__):
    #    print ("Found submodule %s (is a package: %s)" % (modname, ispkg))
    #print(pykiss.decode_dataframe(data))
    #print(aprspy.APRS.parse(data))


if __name__ == '__main__':
    main()
    
