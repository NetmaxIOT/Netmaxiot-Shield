#!/usr/bin/env python
# PIR Sensor For Netmax iot Shield
# :) my PIR Sensor 
# PIR Sensor Example By NetmaxIOT  & Rohitkhosla
# OpenSource MIT licence by Netmax iot Shield And Rohitkhosla
# :)

# retriggerable means the sensor will continue outputting high if motion was detected before the hold timer expires.
# non-retriggerable means the sensor will output high for the specified hold time only, then output low until motion is detected again.
# if there is constant motion detected, retriggerable will stay high for the duration and non-retriggerable will oscillate between high/low.

import time
import Netmaxiot

# Connect the Netmaxiot PIR Motion Sensor to digital pin 8
# NOTE: Some PIR sensors come with the SIG line connected to the yellow wire and some with the SIG line connected to the white wire.
# If the example does not work on the first run, try changing the pin number
# For example, for port D8, if pin 8 does not work below, change it to pin 7, since each port has 2 digital pins.
# For port 4, this would pin 3 and 4
pir_sensor = 8
motion=0
Netmaxiot.pinMode(pir_sensor,"INPUT")
while True:
	try:
		# Sense motion, usually human, within the target range
		motion=Netmaxiot.digitalRead(pir_sensor)
		if motion==0 or motion==1:	# check if reads were 0 or 1 it can be 255 also because of IO Errors so remove those values
			if motion==1:
				print ('Motion Detected')
			else:
				print ('-')
			# if your hold time is less than this, you might not see as many detections
		time.sleep(.2)
	except IOError:
		print ("Error")
