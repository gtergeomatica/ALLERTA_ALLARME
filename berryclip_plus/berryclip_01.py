#!/usr/bin/python
#--------------------------------------   
#    ___                   ________        __
#   / _ )___ __________ __/ ___/ (_)__  __/ /_
#  / _  / -_) __/ __/ // / /__/ / / _ \/_  __/
# /____/\__/_/ /_/  \_, /\___/_/_/ .__/ /_/
#                  /___/        /_/ 
#  
#       BerryClip+ - 6 LED Board
#
# This script lights all 6 LEDs,
# useful for testing ONLY the leds
#
# Author : Matt Hawkins
# Date   : 01/11/2013
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import required libraries
import RPi.GPIO as GPIO
import time

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

# List of LED GPIO numbers
LedSeq = [4,17,22,10,9,11]

# Set up the GPIO pins as outputs and set False
print "Setup LED pins as outputs"
for x in range(6):
    GPIO.setup(LedSeq[x], GPIO.OUT)
    GPIO.output(LedSeq[x], False)

# Light all the leds
for x in range(6):
    GPIO.output(LedSeq[x], True)    
    time.sleep(0.2)

raw_input('All 6 leds should now be lit, press enter to exit program')

# Reset GPIO settings
GPIO.cleanup()