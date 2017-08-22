#!/usr/bin/env python

# ____________________________________________________
# :) My  Button Netmaxiot interfacing 
# Button Example By NetmaxIOT  & Rohitkhosla
# OpenSource MIT licence by Netmax IOT Shield And Rohitkhosla
# :)
#------------------------------------------------------------
import time
import Netmaxiot
# Connect the Netmaxiot Button to digital port D3
# SIG,NC,VCC,GND
button = 3
Netmaxiot.pinMode(button,"INPUT")
while True:
    try:
        print(Netmaxiot.digitalRead(button))
        time.sleep(0.2)

    except IOError:
        print ("Error")
