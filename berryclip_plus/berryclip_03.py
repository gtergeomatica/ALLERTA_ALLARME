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
# This script tests the two switches.
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

print "Setup GPIO pins as inputs and outputs"

# Set Switches GPIO as input
GPIO.setup(7 , GPIO.IN)
GPIO.setup(25, GPIO.IN)

print "Press a button"

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:

  # Loop until users quits with CTRL-C
  while True :
   
    if GPIO.input(7)==1:
      print "  Button S1 pressed!"
      time.sleep(0.5)
      print "Press a button (CTRL-C to exit)"

    if GPIO.input(25)==1:
      print "  Button S2 pressed!"
      time.sleep(0.5)
      print "Press a button (CTRL-C to exit)"
      
except KeyboardInterrupt:
  # Reset GPIO settings
  GPIO.cleanup()