"""
author: Heecheon Park
Marine Lab Project
Language: Python 2.7
Description:
    This is a base program to receive signals from Arduino.
    Signal is converted to a string and concatenate with a datetime object
    to record a timestamp for each data received.
"""

import serial
import datetime

ser = serial.Serial('/dev/ttyUSB0',9600)
s = [0]
while True:
        str1 = str(ser.readline())
        str1 = str1.replace('\n', ' ').replace('\r', '')
        print str1+str(datetime.datetime.now())[:16]

