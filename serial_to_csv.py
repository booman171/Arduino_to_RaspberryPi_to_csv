from __future__ import print_function
from time import ctime
import time
import csv
import serial

# use the command 'ls /dev/tty*' to deter,ine the com port
# for your device. in my case it is ttyACM0, as below
ser = serial.Serial('/dev/ttyACM0')
ser.flushInput()

# Sets a unique filename or each session
filename = "data_" + str(time.time()) + ".csv"
f = open(filename, "a")
f.write("Epoch,Pitch,Roll,Yaw,Pulse,Temp" + "\n")
f.close
while True:
    # Read in Serial line
    ser_bytes = ser.readline()
    #ser_bytes = ser_bytes.replace("b", "")
    message = str(ser_bytes)

    message = message.replace("b", "")
    message = message.replace("r", "")
    message = message.replace("n'", "")
    message = message.replace("\\", "")
    message = message.replace("\'", "")

    print(message)

    # Keep file open to write to
    with open(filename, "a") as f:
        # Writes to file separated by commas
        f.write(str(time.time()) + "," +  message + "\n")
