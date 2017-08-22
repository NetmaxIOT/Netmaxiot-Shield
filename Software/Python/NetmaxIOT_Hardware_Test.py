#!/usr/bin/env python
# ____________________________________________________
# :) MY Netmaxiot Hardware Test interfacing library 
#  HaRDWARE By NetmaxIOT  & Rohitkhosla   Tadaaaaaa
# OpenSource MIT licence by Netmax IOT Shield And Rohitkhosla
# :)
#----------------------------------------------------------------

import time
import Netmaxiot

# Connect the Netmaxiot Button to Analog Port 0.
button = 14		# This is the A0 pin.
buzzer = 8		# This is the D8 pin.

Netmaxiot.pinMode(button,"INPUT")
Netmaxiot.pinMode(buzzer,"OUTPUT")

print("Netmaxiot Basic Hardware Test.")
print("Setup:  Connect the button sensor to port A0.  Connect a simple Buzzer to port D8.")
print("Press the button on Netmax iot Shield and the buzzer will buzz tadaaaaaa!")
time.sleep (4.0)

while True:
    try:
		butt_val = Netmaxiot.digitalRead(button)	# Each time we go through the loop, we read A0.
		print (butt_val) # Print the value of A0 huhaaaaa hahaha :)
		if butt_val == 1:
			Netmaxiot.digitalWrite(buzzer,1)
			print ('start')
			time.sleep(1)
		else:
			Netmaxiot.digitalWrite(buzzer,0)
			time.sleep(.5)

    except IOError:
        print ("Error")
