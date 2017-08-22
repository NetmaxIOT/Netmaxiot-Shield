#!/usr/bin/env python
#
import time
import Netmaxiot

# Connect the Netmaxiot Switch to digital port D3
# SIG,NC,VCC,GND
switch = 3

Netmaxiot.pinMode(switch,"INPUT")

while True:
    try:
        print(Netmaxiot.digitalRead(switch))
        time.sleep(.5)

    except IOError:
        print ("Error")
