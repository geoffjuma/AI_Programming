	#!/usr/bin/env python
from socket import *

def myConnection():
	PORT = 80
	mysocket = socket(AF_INET,SOCK_STREAM)
	host = 'localhost'
	mysocket.bind((host,PORT))
	mysocket.listen(5)
	while True:
		conn, addr = mysocket.accept()
		print 'Got a connection from', addr
		conn.send( 'How can I help you? Choose options Y/N')
		choice = conn.recv(1024)
		if (choice == 'N'):
			conn.send( 'You have chosen N')
			conn.send( 'System quiting. Thank you')
		else:
			conn.send( 'OK! Looks like you need some help')
			conn.send( 'What type of help? Choose options [1/2/3/4/5]')
		conn.close()



myConnection()
		

