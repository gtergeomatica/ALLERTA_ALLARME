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
# This script creates a game that gives
# you a score based on your reaction 
# time
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

def set_leds(status):
  # Set all LEDs to 'status'
  # status is either True or False
  GPIO.output(4 , status)
  GPIO.output(17, status)
  GPIO.output(22, status)
  GPIO.output(10, status)
  GPIO.output(9 , status)
  GPIO.output(11, status)  

def set_leds_half(status):
  # Set half LEDs to 'status'
  # and other half to opposite
  # status is either True or False
  GPIO.output(4 , status)
  GPIO.output(17, status)
  GPIO.output(22, status)
  GPIO.output(10, not status)
  GPIO.output(9 , not status)
  GPIO.output(11, not status) 
  
# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

# Set LED GPIO pins as outputs
GPIO.setup(4 , GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9 , GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

# Set Buzzer GPIO as output
GPIO.setup(8 , GPIO.OUT)
GPIO.output(8 , False)

# Set Switches GPIO as input
print "Setup Switch pin as input"
GPIO.setup(7 , GPIO.IN)
GPIO.setup(25, GPIO.IN)

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:

  # Loop until users quits with CTRL-C
  while True :

    # Turn off LEDs
    set_leds(False)

    print ""
    print ('Press the Red button (S2) to start the game (CTRL-C to exit)')
    print ('The LEDs will flash.')
    print ('When they are all off press the Black button (S1) to measure your reaction time.')

    # Loop until Red button (S2) is pressed
    while GPIO.input(25)==0:    
      pass

    randtime = random.randint(2,15)    
    
    for x in range(randtime):
      # Turn on LEDs
      set_leds_half(True)  
      time.sleep(0.5)
      # Turn off LEDs
      set_leds_half(False)  
      time.sleep(0.5)
      
    # Turn off LEDs
    set_leds(False)    
      
    start = time.time()
    
    # Loop until Black button (S1) is pressed    
    while GPIO.input(7)==0:    
      pass
      
    stop = time.time()
    mytime = (stop-start)*1000
    mytime = round(mytime)

    print ""
    print "Your time was " + str(mytime) + " milliseconds"
    print ""
      
except KeyboardInterrupt:
  # Reset GPIO settings
  GPIO.cleanup()