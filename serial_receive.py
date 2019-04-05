#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
author: Heecheon Park
title: MSUM Marine Lab tide-pool db manager
description: 
    This is a code base to manage a database 
    based on data received from Arduino.
    
    It has been tested to work with basic functionalities.

    The basic functionalities is as follow:
        1. import pymysql, if not exists, install PyMySQL module.
        2. Connect to mysqldb without any databse. (This can be modified if a database already exists).
        3. Create db and table.
        4. Close the db.
note:
    The basic test was done under UNIX environment.
"""
import serial
import datetime
import subprocess
import os

try:
    import pymysql
    import getpass
except ImportError:
    print("This program requires PyMySQL and getpass libraries.")
    print("Install PyMySQL/getpass first by typing: pip3 install PyMySQL or getpass")
    print("Alternatively, python3 -m pip install PyMySQL (or getpass)")
    exit()


def setupCursor():
    db_name = "MARINELAB_DB"
    username = input("MySQL username: ")
    password = str(getpass.getpass("MySQL password: "))
    db = pymysql.connect(host="localhost", port=3306, user=username, passwd=password, autocommit=True)

    return db.cursor()

def insertData(cursor, *args):
    
    query = """
            INSERT INTO DATA 
            (
                WATER_LEVEL_A, 
                WATER_LEVEL_B, 
                TOTAL_VOLUME, 
                TIDE, 
                TEMPERATURE, 
                TIME_LOG
            ) VALUES
            (
                {0},
                {1},
                {2},
                {3},
                {4},
                NOW()
            )""".format(args[0],args[1],args[2],args[3],args[4])
    cursor.execute(query)

def main():
    cmd = "dmesg |egrep 'attached*' |awk '{ print $NF }'"
    filename = "/home/pi/marinelab_project/arduino_log.txt"
    logCounter = 0

    serialName = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    serialName = str(serialName.communicate()[0].decode("utf-8")).replace('\n', '').replace('\r', '')
    print(serialName)
    ser = serial.Serial('/dev/'+serialName,9600)
    s = [0]

    cursor = setupCursor()
    cursor.execute("USE MARINELAB_DB")
    
    with open(filename, "a") as f:

        while logCounter < 10:
                #read_serial=ser.readline()
                #s[0] = str(int (ser.readline(),16))
                str1 = str(ser.readline().decode("utf-8"))
                str1 = str1.replace('\n', ' ').replace('\r', '')
                parsedStr = str1+','+str(datetime.datetime.now())[:16]
                parsedStrList = parsedStr.split(',')
                print(parsedStrList)
               
                insertData(cursor, parsedStrList[0],parsedStrList[1],parsedStrList[2],parsedStrList[3],parsedStrList[4],parsedStrList[5])
                f.write(parsedStr+'\n')
                logCounter += 1
        f.close()
        print("All the logs have been stored at arduino_log.txt")
        print("Please check if the logging process was successful!")

    table = cursor.fetchall()
    print("Fetching done.... printing values from the table....")
    for value in table:
        print("{0} {1} {2} {3} {4} {5}".format(value[0], 
                value[1], 
                value[2], 
                value[3], 
                value[4], 
                value[5], 
                ))

if __name__ == "__main__":
    main()
