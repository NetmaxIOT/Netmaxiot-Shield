#!/usr/bin/env python

# ____________________________________________________
# :) My  Current Sensor Netmaxiot interfacing 
# Current Sensor Example By NetmaxIOT  & Rohitkhosla
# OpenSource MIT licence by Netmax IOT Shield And Rohitkhosla
# :)
#------------------------------------------------------------

import time
import NetmaxIOT

# Connect the NetmaxIOT Current  Sensor to analog port A0
# SIG,NC,NC,GND
sensor = 0

NetmaxIOT.pinMode(sensor,"INPUT")

# Vcc of the NetmaxIOT interface is normally 5v
Netmaxiot_vcc = 5

while True:
    try:
        # Get sensor value
        sensor_value = NetmaxIOT.analogRead(sensor)

        # Calculate amplitude current (mA)
        amplitude_current = (float)(sensor_value / 1024 * Netmaxiot_vcc / 800 * 2000000)

        # Calculate effective value (mA)
        effective_value = amplitude_current / 1.414

        # minimum_current = 1 / 1024 * Netmaxiot_vcc / 800 * 2000000 / 1.414 = 8.6(mA)
        # Only for sinewave AC current

        print("sensor_value", sensor_value)
        print("The amplitude of the current is", amplitude_current, "mA")
        print("The effective value of the current is", effective_value, "mA")
        time.sleep(1)

    except IOError:
        print ("Error")
