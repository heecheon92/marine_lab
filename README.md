# marine_lab

Minnesota State University, Moorhead

Heecheon Park

Communication between Arduino and Raspberry Pi for Data Logging.

This is a code base and therefore, it is not a completed work.

# Plan

arduino.ino will be compiled and executed to create a communication channel between Arduino and Raspberry Pi.

Arduino is the main controller that controls the circulation of water between the tanks.

This program sends logs to the Pi and the Pi saves the received data a local storage.

Additionally, a Python script can be executed to send command signals to the Arduino, resetting the signal to the relays so 

that the relays can actuate the solenoid valves.



