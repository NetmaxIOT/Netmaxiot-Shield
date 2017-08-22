#!/usr/bin/env python
import time
import Netmaxiot
# Connect the  Relay to digital port D4

relay = 4

Netmaxiot.pinMode(relay,"OUTPUT")

while True:
    try:
        # switch on for 1 seconds
        Netmaxiot.digitalWrite(relay,1)
        print ("on")
	print ("---------------------")
        time.sleep(1)
        # switch off for 1 seconds
        Netmaxiot.digitalWrite(relay,0)
        print ("off")
	print ("---------------------")
        time.sleep(1)
    except KeyboardInterrupt:
        Netmaxiot.digitalWrite(relay,0)
        break
    except IOError:
        print ("Error")
