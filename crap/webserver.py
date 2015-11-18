#!/usr/bin/env python
from socket import *
import os 
import re 

class Requests(object):
	"""docstring for Requests"""
	def __init__(self, host,port):
		super(Requests, self).__init__()
		self.host = host
		self.port = port

	def myConnection(self):
		mysocket = socket(AF_INET,SOCK_STREAM)
		mysocket.bind((self.host,self.port))
		mysocket.listen(5)
		while True:
			conn, addr = mysocket.accept()
			print 'Got a connection from', addr
			req = conn.recv(1024)
			print req
			match = re.match('GET /move\?a=(\d+)\sHTTP/1',req)
			if match :
				angle = match.group
				conn.sendall("""HTTP/1.0 200 OK 
					Content-Type: text/html 
					<html> 
					<head> <title>Success</title> 
					</head> 
					<body> Boo! </body> 
					</html>""")
    		else:
        		# If there was no recognised command then return a 404 (page not found)
        		print "Returning 404"
        		conn.sendall("HTTP/1.0 404 Not Found\r\n")
    			conn.close()

newConnection = Requests('localhost',9010)
newConnection.myConnection()