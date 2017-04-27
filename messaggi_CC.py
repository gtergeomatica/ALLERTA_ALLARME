#!/usr/bin/env python
# Copyleft Gter srl 2017
# roberto.marzocchi@gter.it


# ricezione messaggi da CC con i seguenti campi separati da |:
# - numero_client
# - stringa di 0,1,2 con allerte allarmi
# - sistema degradato
# - allarme generico
# - near alarm
 
'''
    Simple socket server using threads
'''
 
import socket
import sys
import time
import RPi.GPIO as GPIO



# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

timeLed = 0.5;

print "Setup GPIO pins as inputs and outputs"

try:
    # Set LED GPIO pins as outputs
    GPIO.setup(4 , GPIO.OUT) #rosso
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT) #giallo
    GPIO.setup(10, GPIO.OUT)
    GPIO.setup(9 , GPIO.OUT) #verde
    GPIO.setup(11, GPIO.OUT)

    # Set Buzzer GPIO pins as output
    GPIO.setup(8 , GPIO.OUT)

    # Set Switches GPIO as input
    GPIO.setup(7 , GPIO.IN)
    GPIO.setup(25, GPIO.IN)
except: 
    print "Led gia configurati"




from datetime import datetime, date

HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 8082 # Arbitrary non-privileged port
BUFFER_SIZE = 1024 



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)





while True:
    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        #s.close()
        #sys.exit()
        continue
    break
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'

# set non blocking mode per gestire l'accept con un try-except
s.setblocking(0)

start = time.time()
print start
GPIO.output(4 , False) 
GPIO.output(17 , False)
GPIO.output(22 , False)
GPIO.output(10, False)
GPIO.output(9, False)
GPIO.output(11, False)

GPIO.output(8, False)


time.sleep(timeLed)
#GPIO.output(4 , True)
#GPIO.output(9 , True)
#GPIO.output(22, True)

#quit()

#now keep talking with the client
while True:
    #GPIO.output(4 , False)
    #GPIO.output(9 , False)
    #GPIO.output(22, False)



    #wait to accept a connection - blocking call
    #da testare se il server non manda dati come nitarlo accendendo comunque una luce...
    #print "fin qua ci arriva"
    try:    
        conn, addr = s.accept()
    except: 
        done = time.time()
        differenza = done-start
        if differenza > 3:
            GPIO.output(4 , False)
            GPIO.output(9 , False)
            GPIO.output(22, False)
            try:
                GPIO.output(8, False)
            except:
                print ""      
            time.sleep(timeLed)
            print "Ritardo > 3 secondi... "
            GPIO.output(4 , True)
            GPIO.output(9 , True)
            GPIO.output(22, True)
            time.sleep(timeLed)
        continue
    #break
    #print conn    
    # calcolo ora UTC nello stesso formato dell'output di RTKLIB
    dt=datetime.utcnow()
    #sovrascrivo il time start per il check sul funzionamento degradato
    start = time.time()
    # Formatting datetime
    ora=dt.strftime("%Y/%m/%d|%H:%M:%S.%f")
    print ora
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    #data = unicode(conn.recv(BUFFER_SIZE))
    data = conn.recv(BUFFER_SIZE)            
    dati=data.split('|')
    print data
    stringa=dati[1]
    print "dati0=",dati[0]
    print stringa
    i=0
    allarme=-1
    GPIO.output(22 ,False)
    GPIO.output(9 , False)
    GPIO.output(4 , False)
    #GPIO.output(11 , False)
    GPIO.output(10 ,False)
    GPIO.output(17 ,False)    
    time.sleep(timeLed)
    #cerco gli allarmi dell'algoritmo
    while (i<int(dati[0])):
        #print stringa[i]
        if (int(stringa[i])>=0):
            #devo gestire gli allarmi
            if (allarme<=1):
                allarme=int(stringa[i])
            else:                 
                allarme=2
        i=i+1
    print "allarme=",allarme
    if allarme==0:
        print "accendo il verde"
        GPIO.output(8 , False)      
        GPIO.output(4 , False)
        GPIO.output(22 , False)
        GPIO.output(9 , True)
    elif (allarme==1):
        print "accendo il giallo"
        GPIO.output(4 , False)
        GPIO.output(9 , False)
        GPIO.output(22, True)
        GPIO.output(8 , True)
    elif allarme==2:
        print "accendo il ROSSO e il buzzer"
        GPIO.output(22 , False)
        GPIO.output(9, False)         
        GPIO.output(8 , True)
        GPIO.output(4 , True)
    # cerco funzionamento degradato
    if int(dati[2])==1:
        GPIO.output(10 , True)
    else:
        GPIO.output(10 , False)

    # cerco allarme generico
    if int(dati[3])>0:
        GPIO.output(17 , True)
        GPIO.output(8 , True)
    elif allarme>0:
        print "accendo l'altro rosso"
        GPIO.output(17 , False)
    else :
        print "spengo il buffer"
        GPIO.output(17 , False)
        GPIO.output(8 , False)

    # cerco near alarm
    if (int(dati[4])>0 and allarme==0):
        GPIO.output(17 , True)
    else :
        GPIO.output(17 , False)
        
    time.sleep(timeLed)
    conn.send('OK\0')

s.close()



quit()


#socket data
TCP_IP = '192.168.2.126'
TCP_PORT = 8082
BUFFER_SIZE = 1024
check_connection=0



while True:  
    try:
        if (check_connection==0):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TCP_IP, TCP_PORT))
        #s.send(MESSAGE)
        data = s.recv(BUFFER_SIZE)
        #s.close()
        check_connection=1
        print "received data:", data
    except: 
        print "Connessione socket non riuscita"
        check_connection=0   
    #time.sleep(0.5)
