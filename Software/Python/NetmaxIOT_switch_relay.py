#!/usr/bin/env python
# Netmax switch example with iot port good one :)

import time
import Netmaxiot

# Connect the Netmaxiot Switch to digital port D3
# SIG,NC,VCC,GND
switch = 3

# Connect the Netmaxiot Relay to digital port D4
# SIG,NC,VCC,GND
relay = 4

Netmaxiot.pinMode(switch,"INPUT")
Netmaxiot.pinMode(relay,"OUTPUT")

while True:
    try:
        if Netmaxiot.digitalRead(switch):
            Netmaxiot.digitalWrite(relay,1)
        else:
            Netmaxiot.digitalWrite(relay,0)

        time.sleep(.5)

    except KeyboardInterrupt:
        Netmaxiot.digitalWrite(relay,0)
        break
    except IOError:
        print ("Error")
