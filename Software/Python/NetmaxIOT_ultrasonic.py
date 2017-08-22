#!/usr/bin/env python

import Netmaxiot
# Connect the Netmaxiot Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND
ultrasonic_ranger = 4
while True:
    try:
        # Read distance value from Ultrasonic
        print(Netmaxiot.ultrasonicRead(ultrasonic_ranger))
    except TypeError:
        print ("Error")
    except IOError:
        print ("Error")


