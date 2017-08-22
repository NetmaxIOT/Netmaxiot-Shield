#!/usr/bin/env python
# ____________________________________________________
# :) My Buzzer Netmaxiot Sensor  interfacing 
#  Buzzer By NetmaxIOT  & Rohitkhosla
# OpenSource MIT licence by Netmax IOT Shield And Rohitkhosla
# :)
#----------------------------------------------------------------

import time
import Netmaxiot
# Connect the  Buzzer to digital port D8
# SIG,NC,VCC,GND
buzzer = 4
Netmaxiot.pinMode(buzzer,"OUTPUT")
while True:
    try:
        # Buzz for 1 second
        Netmaxiot.digitalWrite(buzzer,1)
        print ('start')
        time.sleep(2)
        # Stop buzzing for 1 second and repeat
        Netmaxiot.digitalWrite(buzzer,0)
        print ('stop')
        time.sleep(2)

    except KeyboardInterrupt:
        Netmaxiot.digitalWrite(buzzer,0)
        break
    except IOError:
        print ("Error")
