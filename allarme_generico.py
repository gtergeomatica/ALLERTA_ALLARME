#!/usr/bin/python
#   Gter Copyleft 2017
#   Roberto Marzocchi
#
#
#   Modified by an priginal project
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
import requests




#library added by GTER
import os,sys,shutil,re,glob
import socket
#import time
from datetime import datetime, date



#######################################################################################
# questa e' la parte da inizializzare in base a id_apparato e IP centro di controllo
#socket data per inviare dati al CC
#TCP_IP is the address of the control center server (TBM)
#TCP_IP = '192.168.2.126'

# in questo modo gli faccio leggere i dati da terminale (IP address e ID apparato)
#print(sys.argv)
#TCP_IP = sys.argv[1]
# qua specifico l'ID dell'apparato
#id_apparato=sys.argv[2]

#in questo modo leggo invece i messaggi da file 
nomefile1="/home/pi/NARVALO/DATI/CONF/narvalo_conf.dat"
print "\n\nReading the %s file " %nomefile1

# legge dal file coordinate 
parametri=[]

i=0
cc=0
for riga in file(nomefile1): # lettura file 
	#print riga
	#line = riga
	parametri.append(riga.strip('\n'))
	i+=1

id_apparato=parametri[0]
TCP_IP=parametri[2]


print "#######################################"
print "Id apparato:", id_apparato
print "IP CC Anticollisione:", TCP_IP
print "#######################################"

################
# fissi 
TCP_PORT = 8081
BUFFER_SIZE = 1024
check_connection=0




#error_type
error_type=5
#######################################################################################


#headers per inviare dati al CONCENTRATORE

headers1 = {
    'Content-type': 'application/x-www-form-urlencoded',
}
url2 = "http://narvalo.dyndns.org/Narvalo/NarvaloWS/api/Narvalo/SetAllarme"






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
        MESSAGE = "A|1"
        try:
            if (check_connection==0):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((TCP_IP, TCP_PORT))
            s.send(MESSAGE)
            data = s.recv(BUFFER_SIZE)
            #s.close()
            check_connection=1
            print "Messaggio inviato al CC - Risposta:", data
        except:
            print "Socket connection failed!"
            check_connection=0
        try:
            dt=datetime.utcnow()
            # Formatting datetime
            day_time=dt.strftime("%Y%m%d %H:%M:%S")
            #day_time=dt.strftime("%d:%m:%Y %H:%M:%S")
            # invio l'allarme al concentratore
            data1 = {
            'desc': 'Allarme Generico',
            #'IdType': error_type,
            'apparati': id_apparato,
            'utc' : day_time
            }
            print data1;
            r = requests.post(url2, data=data1, headers=headers1)
            result = r.text
            print "Stampo la risposta del concentratore"
            print result
        except:
            print "Concentratore non avvisato" 
        time.sleep(0.5)
        #print "Press a button (CTRL-C to exit)"

    if GPIO.input(25)==1:
        print "  Button S2 pressed!"
        MESSAGE = "A|2"
        try:
            if (check_connection==0):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((TCP_IP, TCP_PORT))
            s.send(MESSAGE)
            data = s.recv(BUFFER_SIZE)
            #s.close()
            check_connection=1
            print "Messaggio inviato al CC - Risposta:", data
        except:
            print "Socket connection failed!"
            check_connection=0
        try:
            dt=datetime.utcnow()
            # Formatting datetime
            day_time=dt.strftime("%Y%m%d %H:%M:%S")
            # invio l'allarme al concentratore
            data1 = {
            'desc': 'Allarme Generico',
            #'IdType': error_type,
            'apparati': id_apparato,
            'utc' : day_time
            }
            r = requests.post(url2, data=data1, headers=headers1)
            result = r.text
            print "Stampo la risposta del concentratore"
            print result
        except:
            print "Concentratore non avvisato"
        time.sleep(0.5)
        #print "Press a button (CTRL-C to exit)"
      
except KeyboardInterrupt:
  # Reset GPIO settings
  GPIO.cleanup()
