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
# This script randomly lights LEDs.
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
import random

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

# List of LED GPIO numbers
LedSeq = [4,17,22,10,9,11]

# Set up the GPIO pins as outputs and set False
print "Setup LED pins as outputs"
for x in range(6):
  GPIO.setup(LedSeq[x], GPIO.OUT)
  GPIO.output(LedSeq[x], False)

# Seed the random number generator
random.seed()

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:

  # Loop until users quits with CTRL-C
  while True :
     
    # Turn off all 6 LEDs
    for x in range(6):
      GPIO.output(LedSeq[x], False)      
      
    # Generate random number between 0 and 5
    result = random.randint(0,5)
    print "Turn on LED : " + str(result)
    # Turn LED number X  
    GPIO.output(LedSeq[result], True)  

    # Wait
    time.sleep(0.2)
      
except KeyboardInterrupt:
  # Reset GPIO settings
  GPIO.cleanup()