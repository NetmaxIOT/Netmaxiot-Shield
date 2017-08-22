#!/usr/bin/env python



# 		Min  Typ  Max  Condition
# 		0    0    0    sensor in open air
# 		0    20   300  sensor in dry soil
# 		300  580  700  sensor in humid soil
# 		700  940  950  sensor in water
	
# 	Sensor values observer: 
# 		Val  Condition
# 		0    sensor in open air
# 		18   sensor in dry soil
# 		425  sensor in humid soil
# 		690  sensor in water

import time
import Netmaxiot

# Connect the Netmaxiot Moisture Sensor to analog port A0
# SIG,NC,VCC,GND
sensor = 0

while True:
    try:
        print(Netmaxiot.analogRead(sensor))
        time.sleep(.5)

    except KeyboardInterrupt:
        break
    except IOError:
        print ("Error")
