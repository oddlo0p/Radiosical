# More features (modules) added using 'import' function
import serial
import threading
import time
import sys

# Name of the port
port = '/dev/cu.usbserial-AM008HT2'
# The baud (bits transferred per second) of the port
baud = 2400

# Handle/Variable for the serial port to communicate with the port
serial_port = serial.Serial(port, baud, timeout=0)

# When a tag is read -> Data tag shown in terminal

data_number = str


def handle_data(data):
    data_number = data
    print("data=", data_number)
    return data_number


# Will read the data from the reader and sends that to handle_data
def read_from_port(ser):
    new_data = ""
    while True:
        reading = ser.read(1)
        if len(reading) > 0:
            if b'\r' == reading:
                handle_data(new_data)
                new_data = ""
            elif b'0' <= reading <= b'F':
                new_data = new_data + reading.decode()


# Creating a thread to manage the workflow and to allow pygame
thread = threading.Thread(target=read_from_port, args=(serial_port,))
thread.start()

print("Go ahead and wave a tag near the reader.")

# To have an infinite loop of code
while True:
    a = 0
