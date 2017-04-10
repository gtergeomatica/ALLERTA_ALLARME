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
# This script lights the 6 LEDs in
# sequence, 1 LED at a time.
#
# Author : Matt Hawkins
# Date   : 01/11/2013
#
# http://www.raspberrypi-spy.co.uk/
#
#-------------------------------------- 

# Import required libraries
import RPi.GPIO as GPIO
import sys
import time

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

# List of LED GPIO numbers
LedSeq = [4,17,22,10,9,11]

# Get delay from command line or set default
if len(sys.argv)==2:
  delay = float(sys.argv[1])
else:
  delay = 0.08

# Set up the GPIO pins as outputs and set False
print "Setup Outputs"
for x in range(6):
  GPIO.setup(LedSeq[x], GPIO.OUT)
  GPIO.output(LedSeq[x], False)

# Set step size and direction
step=1

seq_count=0

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:

  # Loop until users quits with CTRL-C
  while True:

    # Loop through sequence 0 to 9
    # and 9 to 0  
    while seq_count<6 and seq_count>=0:
      # Delay
      time.sleep(delay)
      print "SEQ : %i" %seq_count
      # Loop through each LED
      for y in range(6) :
        if y==seq_count :
          # This LED is ON
          GPIO.output(LedSeq[y], True)
        else:
          # This LED is OFF
          GPIO.output(LedSeq[y], False)

      # Move the sequence one step
      seq_count += step
    
    # Invert the step so sequence runs
    # in opposite direction
    step = step * -1
    print " Step : %i" %step

    # Correct sequence count by 2 steps
    seq_count=seq_count + step + step
      
except KeyboardInterrupt:
  # Reset GPIO settings
  GPIO.cleanup()