#!/usr/bin/python3
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
try:
    import pymysql
except ImportError:
    print("Install PyMySQL first by typing: pip3 install PyMySQL")

db_name = "MARINELAB_DB"
username = input("MySQL username: ")
password = str(input("MySQL password: "))

# Open database connection
db = pymysql.connect(host="localhost", port=3306, user=username, passwd=password)

# Prepare a cursor object cursor() method.
cursor = db.cursor()

# Create a test db MARINELAB_DB
try:
    cursor.execute("CREATE DATABASE " + db_name)
except pymysql.err.ProgrammingError:
    print("DB already exists!")

# Use the test db
cursor.execute("USE " + db_name)

# Drop table if it already exist using execute() method.
# This is for a testing purpose.
cursor.execute("DROP TABLE IF EXISTS DATA")

# Create table as per requirement
sql = """
        CREATE TABLE DATA
        (
            WATER_LEVEL CHAR(20) NOT NULL,
            TEMPERATURE CHAR(20),
            TIME_LOG DATETIME
        )
"""

cursor.execute(sql)

# Disconnect from server
db.close()
