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
# This script simulates a traffic light
# using the 6 LEDs and the switch
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
for Led in LedSeq:
    GPIO.setup(Led, GPIO.OUT)
    GPIO.output(Led, False)

# Setup switch as an input
print "Setup Switch as input"
GPIO.setup(7, GPIO.IN)    
    
# Define Function to set state of LEDs and add a delay
def Lights(red1,red2,yellow1,yellow2,green1,green2,delay):
  time.sleep(delay)
  GPIO.output(LedSeq[0], red1) 
  GPIO.output(LedSeq[1], red2) 
  GPIO.output(LedSeq[2], yellow1) 
  GPIO.output(LedSeq[3], yellow2) 
  GPIO.output(LedSeq[4], green1) 
  GPIO.output(LedSeq[5], green2)     
  time.sleep(delay)
    
# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:

  # Light Green Lights
  Lights(False,False,False,False,True,True,0)
  
  CurrentState = 'GO'
  print "The Current State is " + CurrentState
  
  # Loop until users quits with CTRL-C
  while True :
   
    if GPIO.input(7)==1:
      if CurrentState == 'GO':
        # Start 'STOP' sequence

        # Amber
        Lights(False,False,True,True,False,False,2)
        # Red
        Lights(True,True,False,False,False,False,0)

        CurrentState = 'STOP'
        print "The Current State is " + CurrentState
      else:
        # Start 'GO' sequence
        
        # Red + Amber
        Lights(True,True,True,True,False,False,2)        
        # Green
        Lights(False,False,False,False,True,True,0)        

        CurrentState = 'GO'
        print "The Current State is " + CurrentState        
      
except KeyboardInterrupt:
  # Reset GPIO settings
  GPIO.cleanup()
