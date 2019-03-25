import serial
import datetime
import subprocess

cmd = "dmesg |egrep 'attached*' |awk '{ print $NF }'"
serialName = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
serialName = str(serialName.communicate()[0]).replace('\n', '').replace('\r', '')

ser = serial.Serial('/dev/'+serialName,9600)
s = [0]
while True:

        str1 = str(ser.readline())
        str1 = str1.replace('\n', ' ').replace('\r', '')
        print str1+str(datetime.datetime.now())[:16]

