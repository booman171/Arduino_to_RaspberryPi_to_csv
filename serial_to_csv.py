from __future__ import print_function
from time import ctime
import time
import csv
import serial

# use the command 'ls /dev/tty*' to deter,ine the com port
# for your device. in my case it is ttyACM0, as below
ser = serial.Serial('/dev/ttyUSB1')
ser.flushInput()

# Sets a unique filename or each session
filename = "data_" + str(time.time()) + ".csv"

while True:
    # Read in Serial line
    ser_bytes = ser.readline()
    #ser_bytes = ser_bytes.replace("b", "")
    message = str(ser_bytes)
    message = message.replace("b", "")
    message = message.replace("r", "")
    message = message.replace("n", "")
    message = message.replace("\\", "")
    message = message.replace("\'", "")

    # Decodes the line to a better format
    #decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
    print(message)
    # Splits the line by commas to a list of Strings
    #values = decoded_bytes.split(",")
    
    # Converts list Strings to floats
    #list(map(float, values))
    
    # Keep file open to write to
    with open(filename, "a") as f:
        # Writes to file separated by commas
        f.write(ctime() + "," +  message + "\n")
