#!/usr/bin/env python

# ____________________________________________________
# :) MY Universal Gas Sensor Netmaxiot  interfacing library 
#  Universal Gas Sensor interfacing By NetmaxIOT  & Rohitkhosla   Tadaaaaaa
# OpenSource MIT licence by Netmax IOT Shield And Rohitkhosla
# :)
#----------------------------------------------------------------

# NOTE:
# Different Type of Gas sensors
# MQ2 - Combustible Gas, Smoke
# MQ3 - Alcohol Vapor
# MQ5 - LPG, Natural Gas, Town Gas
# MQ9 - Carbon Monoxide, Coal Gas, Liquefied Gas
# 02 - Oxygen
# The sensitivity can be adjusted by the onboard potentiometer


import time
import Netmaxiot

# Connect the Netmaxiot Gas Sensor to analog port A0
# SIG,NC,VCC,GND

gas_sensor = 0
Netmaxiot.pinMode(gas_sensor,"INPUT")
while True:
    try:
        # Get sensor value
        sensor_value = Netmaxiot.analogRead(gas_sensor)

        # Calculate gas density - large value means more dense gas
        density = sensor_value*100 / 1023
        print "----------------------------------------------------"
        print " "
        print ("sensor_value =", sensor_value, " density =", density)
        print " "
        print "----------------------------------------------------"
        time.sleep(.5)
    except IOError:
        print ("Error")
