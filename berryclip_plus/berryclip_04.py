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
# This script lights the 6 LEDs in sequence
# when the a switch is pressed.
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

# Set LED GPIO pins as outputs
GPIO.setup(4 , GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9 , GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

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

    # Turn off LEDs
    GPIO.output(4 , False)
    GPIO.output(17, False)
    GPIO.output(22, False)
    GPIO.output(10, False)
    GPIO.output(9 , False)
    GPIO.output(11, False)
   
    if GPIO.input(7)==1:
      print "  Button S1 pressed!"
        
      # Turn off LEDs
      GPIO.output(4 , False)
      GPIO.output(17, False)
      GPIO.output(22, False)
      GPIO.output(10, False)
      GPIO.output(9 , False)
      GPIO.output(11, False)
        
      # Turn on LEDs in sequence
      GPIO.output(4 , True)
      time.sleep(0.5)
      GPIO.output(17, True)
      time.sleep(0.5)
      GPIO.output(22, True)
      time.sleep(0.5)
      GPIO.output(10, True)
      time.sleep(0.5)
      GPIO.output(9 , True)
      time.sleep(0.5)
      GPIO.output(11, True)
      
      # Wait 2 seconds
      time.sleep(2)
      
      print "Press a button (CTRL-C to exit)"      
      
    if GPIO.input(25)==1:
      print "  Button S2 pressed!"
        
      # Turn off LEDs
      GPIO.output(4 , False)
      GPIO.output(17, False)
      GPIO.output(22, False)
      GPIO.output(10, False)
      GPIO.output(9 , False)
      GPIO.output(11, False)
        
      # Turn on LEDs in reverse sequence
      GPIO.output(11, True)
      time.sleep(0.5)
      GPIO.output(9 , True)
      time.sleep(0.5)
      GPIO.output(10, True)
      time.sleep(0.5)
      GPIO.output(22, True)
      time.sleep(0.5)
      GPIO.output(17, True)
      time.sleep(0.5)
      GPIO.output(4 , True)
      
      # Wait 2 seconds
      time.sleep(2)
      
      print "Press a button (CTRL-C to exit)"
      
except KeyboardInterrupt:
  # Reset GPIO settings
  GPIO.cleanup()