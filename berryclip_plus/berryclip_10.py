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
# This script outputs a set of light
# sequences. When the switch is pressed
# the sequence speed is toggled.
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

def SoundBuzzer(channel):
  print "  Button pressed!"
  # Turn Buzzer on
  GPIO.output(8, True)
  time.sleep(0.1)
  # Turn Buzzer off
  GPIO.output(8, False)

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

# Set Switches GPIO as input
GPIO.setup(7 , GPIO.IN)
GPIO.setup(25, GPIO.IN)

GPIO.add_event_detect(7, GPIO.FALLING, callback=SoundBuzzer, bouncetime=500)
GPIO.add_event_detect(25, GPIO.FALLING, callback=SoundBuzzer, bouncetime=500)

# Configure GPIO8 as an outout
GPIO.setup(8, GPIO.OUT)
GPIO.output(8, False)

# List of LED GPIO numbers
LedSeq = [4,17,22,10,9,11]

# Set up the GPIO pins as outputs and set False
print "Setup Outputs"
for x in range(6):
  GPIO.setup(LedSeq[x], GPIO.OUT)
  GPIO.output(LedSeq[x], False)

Seq1 = [[1,0,0,0,0,0],
        [0,1,0,0,0,0],
        [0,0,1,0,0,0],
        [0,0,0,1,0,0],
        [0,0,0,0,1,0],
        [0,0,0,0,0,1]]

Seq2 = [[1,1,1,0,0,0],[1,1,1,0,0,0],[0,0,0,1,1,1],[0,0,0,1,1,1]]

Seq3 = [[1,0,0,0,0,1],[0,1,0,0,1,0],[0,0,1,1,0,0],[0,1,0,0,1,0]]

Seq4 = [[0,0,0,0,0,0],
        [0,0,0,0,0,1],
        [0,0,0,0,1,1],
        [0,0,0,1,1,1],
        [0,0,1,1,1,1],
        [0,1,1,1,1,1],
        [1,1,1,1,1,1],
        [0,1,1,1,1,1],
        [0,0,1,1,1,1],
        [0,0,0,1,1,1],
        [0,0,0,0,1,1],
        [0,0,0,0,0,1]]

Seq5 = [[1,1,0,0,0,0],
        [0,1,1,0,0,0],
        [0,0,1,1,0,0],
        [0,0,0,1,1,0],
        [0,0,0,0,1,1],
        [1,0,0,0,0,1]]

Seq6 = [[1,0,1,0,1,0],[1,0,1,0,1,0],[0,1,0,1,0,1],[0,1,0,1,0,1]]

Seq7 = [[1,0,0,0,0,0],
        [0,1,0,0,0,0],
        [0,0,1,0,0,0],
        [0,0,0,1,0,0],
        [0,0,0,0,0,1],
        [0,0,0,0,1,0],
        [0,0,0,1,0,0],
        [0,0,1,0,0,0],
        [0,1,0,0,0,0]]

Seq8 = [[1,1,0,0,1,1],[0,0,1,1,0,0],[1,1,0,0,1,1],[0,0,1,1,0,0]]

Seq9 = [[0,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,1,0,0,0,0],
        [1,1,1,0,0,0],
        [1,1,1,1,0,0],
        [1,1,1,1,1,0],
        [1,1,1,1,1,1],
        [1,1,1,1,1,0],
        [1,1,1,1,0,0],
        [1,1,1,0,0,0],
        [1,1,0,0,0,0],
        [1,0,0,0,0,0]]

# Populate list with all sequences
Seq = [Seq1,Seq2,Seq3,Seq4,Seq5,Seq6,Seq7,Seq8,Seq9]

SeqNumber = 0
Counter   = 0

MaxCycles = 3
MinDelay  = 0.2

print "----------"

try:

  CurrentSeq = Seq[SeqNumber]

  while 1:

    print "Sequence " + str(SeqNumber)
    while Counter<MaxCycles:
      for x in range(len(CurrentSeq)) :
        Leds = CurrentSeq[x]
        for y in range(6) :
          GPIO.output(LedSeq[y], Leds[y])
        time.sleep(MinDelay)
      Counter = Counter + 1
    Counter = 0
    SeqNumber = SeqNumber + 1
    if SeqNumber>=len(Seq):
      SeqNumber = 0
      print "----------"
    CurrentSeq = Seq[SeqNumber]

except KeyboardInterrupt:
  print "Goodbye!"
  # Reset GPIO settings
  GPIO.cleanup()