#!/usr/bin/env python

#:) 
# My Latching Relay interfacing  -
# Latching Relay Example By NetmaxIOT  & Rohitkhosla
# OpenSource MIT licence by Netmax IOT Shield And Rohitkhosla
# ----------------------------------------------------------- 
#:) 


import time
import Netmaxiot

# Connect the Netmaxiot 2-Coil Latching Relay to digital port D4
# SIG,NC,VCC,GND
relay = 4

Netmaxiot.pinMode(relay,"OUTPUT")

while True:
    try:
        # switch on for 5 seconds
        Netmaxiot.digitalWrite(relay,1)
        print ("on")
        time.sleep(5)

        # switch off for 5 seconds
        Netmaxiot.digitalWrite(relay,0)
        print ("off")
        time.sleep(5)

    except KeyboardInterrupt:
        Netmaxiot.digitalWrite(relay,0)
        break
    except IOError:
        print ("Error")
