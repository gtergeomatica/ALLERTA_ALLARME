#!/usr/bin/env python
# Copyleft Gter srl 2017
# roberto.marzocchi@gter.it



'''
    Simple socket server using threads
'''
 
import socket
import sys
import time
from datetime import datetime, date

HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 8082 # Arbitrary non-privileged port
BUFFER_SIZE = 1024 



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
 
#now keep talking with the client
while True:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    #print conn    
    # calcolo ora UTC nello stesso formato dell'output di RTKLIB
    dt=datetime.utcnow()
    # Formatting datetime
    ora=dt.strftime("%Y/%m/%d|%H:%M:%S.%f")
    print ora
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    #data = unicode(conn.recv(BUFFER_SIZE))
    data = conn.recv(BUFFER_SIZE)
    print data
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
