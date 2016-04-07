#! /usr/bin/env python

import sys
import socket
from socket import *

def userInput():
	choice = sys.stdin.readline()
	return choice


def connecting():
	PORT = 5000
	clientSocket = socket(AF_INET,SOCK_STREAM)
	host = 'localhost'
	clientSocket.connect((host,PORT))
	while True:
		print clientSocket.recv(1024)
		input1 = userInput()
		clientSocket.send(input1)


connecting()
