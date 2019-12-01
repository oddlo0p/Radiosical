import pygame
import playingsound
import serialtag

serialtag.read_from_port()

print("Go ahead and wave a tag near the reader.")

pygame.init()
pygame.mixer.init()

playingsound.play_a_bell(serialtag.data_number)

# To have an infinite loop of code
while True:
    a = 0
