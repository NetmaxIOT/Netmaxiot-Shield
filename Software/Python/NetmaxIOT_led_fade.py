#!/usr/bin/env python


import time
import Netmaxiot
# Connect the Netmaxiot LED to digital port D5
# SIG,NC,VCC,GND
led = 5
# Digital ports that support Pulse Width Modulation (PWM)
# D3, D5, D6
# Digital ports that do not support PWM
# D2, D4, D7, D8
Netmaxiot.pinMode(led,"OUTPUT")
time.sleep(1)
i = 0
while True:
    try:
        # Reset
        if i > 255:
            i = 0

        # Current brightness
        print (i)

        # Give PWM output to LED
        Netmaxiot.analogWrite(led,i)

        # Increment brightness for next iteration
        i = i + 10
        time.sleep(.2)

    except KeyboardInterrupt:
        Netmaxiot.analogWrite(led,0)
        break
    except IOError:
        print ("Error")