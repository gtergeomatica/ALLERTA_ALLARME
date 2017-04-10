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
# This script lights all 6 LEDs and 
# sounds the buzzer when a switch
# is pressed.
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

# Buzzer on GPIO8
print "Setup Buzzer pin as output"
GPIO.setup(8, GPIO.OUT)

# Set Switches GPIO as input
print "Setup Switch pin as input"
GPIO.setup(7 , GPIO.IN)
GPIO.setup(25, GPIO.IN)

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.

print "Press a button (CTRL-C to exit)"

try:

  # Loop until users quits with CTRL-C
  while True :

    if GPIO.input(7)==1 or GPIO.input(25)==1:
      print "Switch pressed!"
      # Enable Buzzer and turn on LEDs
      GPIO.output(8, True)
      for x in range(6):
        GPIO.output(LedSeq[x], True)    
      # Wait for 0.2 seconds
      time.sleep(0.2)
      # Disable Buzzer and turn off LEDs
      GPIO.output(8, False)  
      for x in range(6):
        GPIO.output(LedSeq[x], False)   
      
except KeyboardInterrupt:
  # Reset GPIO settings
  GPIO.cleanup()