# More features (modules) added using 'import' function (used to play sounds)
import time
import pygame
import time

pygame.init()
pygame.mixer.init()

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
        # print (bells[i][2])
        # Does the friendly name in this list match what we're looking for?
        if s == bells[i][1]:
            # Yes! Play the sound.
            bells[i][0].play(loops=0, maxtime=0, fade_ms=0)
            break
