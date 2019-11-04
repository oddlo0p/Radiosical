# More features (modules) added using 'import' function
import serial
import threading
import time
import sys
import pygame

pygame.init()
pygame.mixer.init()

# Name of the port
port = '/dev/cu.usbserial-AM008HT2'
# The baud (bits transferred per second) of the port
baud = 2400

# Handle/Variable for the serial port to communicate with the port
serial_port = serial.Serial(port, baud, timeout=0)


# When a tag is read -> Data tag shown in terminal
def handle_data(data):
    print("data=", data)


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



# ---------------------------------------------------------------

bells = [
	  #                    filename      tag data      friendly
      #                    for the       for the tag   name for
      #                    note          that plays    this note
      #                                  this note
      [pygame.mixer.Sound("220-A.wav"), "2900ADF9CF", "A3"],
      [pygame.mixer.Sound("247-B.wav"), "26008B49F0", "B3"],
      [pygame.mixer.Sound("261-C.wav"), "2900EC752F", "C3"],
      [pygame.mixer.Sound("293-D.wav"), "2900E94A0E", "D3"],
      [pygame.mixer.Sound("329-E.wav"), "2900EAB6B2", "E3"],
      [pygame.mixer.Sound("349-F.wav"), "2900AD998A", "F3"],
      [pygame.mixer.Sound("392-G.wav"), "2900E9EF36", "G3"],
      [pygame.mixer.Sound("440-A.wav"), "2900E98CC2", "A4"],
      [pygame.mixer.Sound("494-B.wav"), "2900E95534", "B4"],
      [pygame.mixer.Sound("523-C.wav"), "2900AD7EFF", "C4"],
      [pygame.mixer.Sound("587-D.wav"), "2900AD4B3E", "D4"]
]

def play_a_sound(s):
    for i in range(0, len(bells)):
        if s == bells[i][2]:
            bells[i][0].play(loops=0, maxtime=0, fade_ms=0)
            break;

sound_data = new_data

if sound_data == "2900ADF9CF":
    play_a_sound("A3")