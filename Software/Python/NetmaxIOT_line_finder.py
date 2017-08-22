#!/usr/bin/env python

import time
import Netmaxiot

# Connect the Netmaxiot Line Finder to digital port D7
# SIG,NC,VCC,GND
line_finder = 7

Netmaxiot.pinMode(line_finder,"INPUT")

while True:
    try:
        # Return HIGH when black line is detected, and LOW when white line is detected
        if Netmaxiot.digitalRead(line_finder) == 1:
            print ("black line detected")
        else:
            print ("white line detected")

        time.sleep(.5)

    except IOError:
        print ("Error")
