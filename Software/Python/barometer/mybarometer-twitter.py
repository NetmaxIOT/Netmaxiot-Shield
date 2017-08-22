#!/usr/bin/python

import smbus
import time
import RPi.GPIO as GPIO
import twitter
import Netmaxiot
import math
from BMP180 import BMP085

sada1 = "sade hight sensor with bmp180 hahahahaha @netmaxtech R="
################################3

api = twitter.Api(
    consumer_key='2Hvjf4eIdXSHM3XzWGVwPAPfx',
    consumer_secret='XTx54wbv0tdAAMUcWgAGneFPgg8bo9pi2oii8V8YLmQ01PI7bD',
    access_token_key='757551887512109056-BueEkNYP27gchWuO01uaUuorQ7vOxiV',
    access_token_secret='XITHMTQpitZq2YSSHmf3enX5cMY0fei8wgnSxnq6Y3GW8'
    )

####################

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the BMP085 and use STANDARD mode (default value)
# bmp = BMP085(0x77, debug=True)
bmp = BMP085(0x77, 1)
# To specify a different operating mode, uncomment one of the following:
# bmp = BMP085(0x77, 0)  # ULTRALOWPOWER Mode
# bmp = BMP085(0x77, 1)  # STANDARD Mode
# bmp = BMP085(0x77, 2)  # HIRES Mode
# bmp = BMP085(0x77, 3)  # ULTRAHIRES Mode

rev = GPIO.RPI_REVISION
if rev == 2 or rev == 3:
    bus = smbus.SMBus(1)
else:
    bus = smbus.SMBus(0)

while 1:

	temp = bmp.readTemperature()
	# Read the current barometric pressure level
	pressure = bmp.readPressure()
	# To calculate altitude based on an estimated mean sea level pressure
	# (1013.25 hPa) call the function as follows, but this won't be very accurate
	# altitude = bmp.readAltitude()
	# To specify a more accurate altitude, enter the correct mean sea level
	# pressure level.  For example, if the current pressure level is 1023.50 hPa
	# enter 102350 since we include two decimal places in the integer value
	altitude = bmp.readAltitude(101325)
	Alt=altitude-190
	print " "
	print"-----------------------------------------------"
	print("Current Temperature: %.2f C" % temp)
	print("Current Pressure:    %.2f hPa" % (pressure / 100.0))
	print("Current Altitude:    %.2f m" % Alt)
	print " "
	time.sleep(3.0)
	out_str2 ="Temp: %d,Height: %d meters , %s" %(temp,Alt,sada1)
	print (out_str2)
	api.PostUpdate(out_str2)
	time.sleep(1000)

