#!/usr/bin/env python

import socket
import sys

# This program is to receive data from Arduino.

TCP_IP = '192.168.1.xxx'    # Currently arbitrary. It will have a fixed value, once all the set up is complete.
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = str(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data

