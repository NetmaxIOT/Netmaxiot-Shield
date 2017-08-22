#!/usr/bin/env python
# :) My Temperature  Sensor  interfacing  thermistor
# Temperature  Sensor  Example By NetmaxIOT  & Rohitkhosla
# OpenSource MIT licence by Netmax IOT Shield And Rohitkhosla
# :)

# OpenSource MIT licence by Netmax iot Shield And Rohitkhosla

# NOTE: 
# 	The sensor uses a thermistor to detect ambient temperature.
# 	The resistance of a thermistor will increase when the ambient temperature decreases.
#	
# 	There are 3 revisions 1.0, 1.1 and 1.2, each using a different model thermistor.
# 	Each thermistor datasheet specifies a unique Nominal B-Constant which is used in the calculation forumla.
#	
# 	The second argument in the Netmaxiot.temp() method defines which board version you have connected.
# 	Defaults to '1.0'. eg.
# 		temp = Netmaxiot.temp(sensor)        # B value = 3975
# 		temp = Netmaxiot.temp(sensor,'1.1')  # B value = 4250
# 		temp = Netmaxiot.temp(sensor,'1.2')  # B value = 4250

import time
import Netmaxiot

# Connect the Netmaxiot Temperature Sensor to analog port A0
# SIG,NC,VCC,GND
sensor = 0

while True:
    try:
        temp = Netmaxiot.temp(sensor,'1.1')
        print("temp =", temp)
        time.sleep(.5)

    except KeyboardInterrupt:
        break
    except IOError:
        print ("Error")
