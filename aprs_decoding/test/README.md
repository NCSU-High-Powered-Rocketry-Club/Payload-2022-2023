# Cursed radio and decoding stuff

## what is aprs?
Automatic Packet Reporting System, it be a protocol for sending data over da radio waves

## what is a TNC/direwolf
TNC = [Terminal Node Controller](https://en.wikipedia.org/wiki/Terminal_node_controller)
It's a thing that can turn the audio data in AX.25 protocol format into actual bytes or whatever
Direwolf is a software replacement for a TNC and it's pretty sweet

# how run?
kissTest.py is what is currently working. It prints out aprs signals from a .wav file (hardcoded at the moment). 

To get live audio, replace the `sox -t wav ISSpkt_full.wav -esigned-integer -b 16 -r 48000 -t raw - |` command with `rtl_fm -f 144.39M -s 48000 -o 4 - | and so on` one and it should work
> more info here https://github.com/wb2osz/direwolf/blob/master/doc/Raspberry-Pi-SDR-IGate.pdf
If you are using 9600 baud you replace -B 1200 in the direwolf command with `-B 9600`

to print to a file, just pipe the stdout like `python kissTest.py > output.txt`

also press `q` to quit kissTest.py gracefully