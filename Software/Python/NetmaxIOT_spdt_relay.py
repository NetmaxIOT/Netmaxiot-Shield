#!/usr/bin/env python

# :) my Relay output 
# Relay  Example By NetmaxIOT  & Rohitkhosla
# OpenSource MIT licence by Netmax IOT Shield And Rohitkhosla
# :)

# NOTE:
# 	Relay is both normally open and normally closed.
# 	When the coil is energised, they will both flip.
# 	LED will illuminate when normally open is closed (and normally closed is open).
import time
import Netmaxiot
# Connect the Netmaxiot SPDT Relay to digital port D4
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
