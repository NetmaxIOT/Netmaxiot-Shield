#!/usr/bin/env python
#------------------------------------------------------------ 
#:) 
# My Dht22  Sensor  interfacing 
# DHT22 Sensor Example By NetmaxIOT  & Rohitkhosla
# OpenSource MIT licence by Netmax IOT Shield And Rohitkhosla
# ----------------------------------------------------------- 
#:)


import Netmaxiot
import math
# Connect the dH22 Netmaxiot Temperature & Humidity Sensor Pro to digital port D4
# This example uses the blue colored sensor.
# SIG,NC,VCC,GND
sensor = 4  # The Sensor goes on digital port 4.

# temp_humidity_sensor_type

blue = 0    # The Blue colored sensor.   IT IS DHT11
white = 1   # The White colored sensor.  IT IS dHT22

while True:
    try:
        # This example uses the blue colored sensor. 
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp,humidity] = Netmaxiot.dht(sensor,blue)  
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
    except IOError:
        print ("Error")
