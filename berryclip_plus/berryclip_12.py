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
# This script sends morse code messages.
# It uses the red LEDs and buzzer.
#
# Author : Matt Hawkins
# Date   : 01/11/2013
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import required libraries
import RPi.GPIO as GPIO
import time, sys

GPIO.setmode(GPIO.BCM)

# short mark, dot or "dit" (.) - "dot duration" is one time unit long
# longer mark, dash or "dah" (-) - three time units long
# inter-element gap between the dots and dashes within a character - one dot duration or one unit long
# short gap (between letters) - three time units long
# medium gap (between words) - seven time units long[1]


morsecode = {
          'A': '.-',    'a': '.-',
          'B': '-...',  'b': '-...',
          'C': '-.-.',  'c': '-.-.',
          'D': '-..',   'd': '-..',
          'E': '.',     'e': '.',
          'F': '..-.',  'f': '..-.',
          'G': '--.',   'g': '--.',
          'H': '....',  'h': '....',
          'I': '..',    'i': '..',
          'J': '.---',  'j': '.---',
          'K': '-.-',   'k': '-.-',
          'L': '.-..',  'l': '.-..',
          'M': '--',    'm': '--',
          'N': '-.',    'n': '-.',
          'O': '---',   'o': '---',
          'P': '.--.',  'p': '.--.',
          'Q': '--.-',  'q': '--.-',
          'R': '.-.',   'r': '.-.',
          'S': '...',   's': '...',
          'T': '-',     't': '-',
          'U': '..-',   'u': '..-',
          'V': '...-',  'v': '...-',
          'W': '.--',   'w': '.--',
          'X': '-..-',  'x': '-..-',
          'Y': '-.--',  'y': '-.--',
          'Z': '--..',  'z': '--..',
          '0': '-----', ',': '--..--',
          '1': '.----', '.': '.-.-.-',
          '2': '..---', '?': '..--..',
          '3': '...--', ';': '-.-.-.',
          '4': '....-', ':': '---...',
          '5': '.....', "'": '.----.',
          '6': '-....', '-': '-....-',
          '7': '--...', '/': '-..-.',
          '8': '---..', '(': '-.--.-',
          '9': '----.', ')': '-.--.-',
          ' ': ' ',     '_': '..--.-'
}

# Define delays
unit_delay = 0.07
symbol_timing = {'.': 1 * unit_delay, '-': 3 * unit_delay}

def SendMessage(message):
  # Function to send text string
  for char in message:

    # Get code from dictionary. Use space for 
    # undefined characters.
    code = morsecode.get(char,' ')
    print    
    if code == ' ':
      delay = 6 * unit_delay    
    else:  
      print char + " = ",
      sys.stdout.flush()
      for symbol in code:
        print symbol,
        sys.stdout.flush()
        SendSymbol(symbol)
        # Inter-symbol delay
        time.sleep(symbol_timing['.'])
      # Inter-character delay
      delay = 2 * unit_delay
      
    time.sleep(delay)
  print
  print
      
def SendSymbol(symbol):
  # Function to send either Dot or Dash
  GPIO.output(8, True)
  GPIO.output(4, True)
  GPIO.output(17, True)  
  # Get duration of symbol from list
  time.sleep(symbol_timing[symbol])
  GPIO.output(8, False)
  GPIO.output(4, False)
  GPIO.output(17, False)   
  
# Configure Buzzer pin GPIO8 as an outout
GPIO.setup(8, GPIO.OUT)
GPIO.output(8, False)    
    
# List of LED GPIO numbers
LedSeq = [4,17,22,10,9,11]

# Set up the LED GPIO pins as outputs
for x in range(6):
  GPIO.setup(LedSeq[x], GPIO.OUT)
  GPIO.output(LedSeq[x], False)  
  
# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will prevent
# the user seeing unnecessary error
# messages.
try:

  while True:

    message = raw_input("Enter message to send : ")
    SendMessage(message)
    
except KeyboardInterrupt:
  # Reset GPIO settings
  GPIO.cleanup()