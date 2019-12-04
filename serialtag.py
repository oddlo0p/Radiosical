import serial
import threading
from playingsound import play_a_sound
import pygame
import time
import sys

pygame.init()
pygame.mixer.init()

port = '/dev/cu.usbserial-AM008HT2'

# This is the data rate of the RFID reader
baud = 2400

# Open a connection to the serial port using the information above
serial_port = serial.Serial(port, baud, timeout=0)


# will get called by the rest of the program when a complete tag comes in from the reader
def handle_data(data):
    print("data=", data)
    play_a_sound(data)


print("Please wave a tag near the reader to play notes.")


def read_from_port(ser):
    # Let's start with an empty storage area for the incoming data
    new_data = ""
    while True:
        # Read in one character
        reading = ser.read(1)
        # If we got one, the 'length' will be 1. If not, we have nothing to look at
        if len(reading) > 0:
            if b'\r' == reading:
                # If the data is complete, call our data handler to do something with it
                handle_data(new_data)
                # clear the storage area and get ready for new data
                new_data = ""
            elif b'0' <= reading <= b'F':
                new_data = new_data + reading.decode()


# read_from_port() is intended to run in the background as a separate thread
thread = threading.Thread(target=read_from_port, args=(serial_port,))
thread.start()

while True:
    a = 0
