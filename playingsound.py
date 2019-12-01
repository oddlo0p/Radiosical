# More features (modules) added using 'import' function (used to play sounds)
import time
import pygame
import sys

pygame.init()
pygame.mixer.init()

# ---------------------------------------------------------------

# This is a better way to make sounds. We preload the sound files
# in lists (we do that earlier in the program) and we can just call
# on pygame's player to play them. The 'play_a_bell()' routine
# just needs to know the short name we assigned the sound. It will find
# it and start the sound playing. It plays in the background and you
# can play multiple sounds at once.
#
# What would happen if you made multiple lists? Or could a list contain
# more than one kind of sound?
#
#
# Each of these lists is a sound, space you might use to store a RFID
# tag ID, and a friendlier name you can use to search. These tags are
# simply examples and they won't work with whatever RFID tags you might
# have. If you use this method, you need to read the data from your own
# RFID reader and tags, and substitute in your own data.
bells = [
    #                    filename      tag data      friendly
    #                    for the       for the tag   name for
    #                    note          that plays    this note
    #                                  this note
    [pygame.mixer.Sound("220-A.wav"), "2900ADF9CF", "A3"],
    [pygame.mixer.Sound("247-B.wav"), "3501D5A782", "B3"],
    [pygame.mixer.Sound("261-C.wav"), "3501D5B02A", "C3"],
    [pygame.mixer.Sound("293-D.wav"), "3501D5B15B", "D3"],
    [pygame.mixer.Sound("329-E.wav"), "3501D5B258", "E3"],
    [pygame.mixer.Sound("349-F.wav"), "3501D5BCE9", "F3"],
    [pygame.mixer.Sound("392-G.wav"), "3501D5BD0B", "G3"],
    [pygame.mixer.Sound("440-A.wav"), "3501D5BEF9", "A4"],
    [pygame.mixer.Sound("494-B.wav"), "3501D5C832", "B4"],
    [pygame.mixer.Sound("523-C.wav"), "3501D5CD2D", "C4"],
    [pygame.mixer.Sound("587-D.wav"), "840033CDA1", "D4"]
]


# given the tag OR the friendly name, start the bell sound. This
# routine searches by the friendly sound name, but if you searched
# the entry for the RFID tag, imagine the possibilities...
def play_a_bell(s):
    # len(bells) tells us how many of those individual lists
    # there are in the list 'bells'. Look at each one.
    # If, for example, the user asks for "C3", look
    # at each list for a "C3" in position 2 of the list.
    # When we see one, start playing the sound file for
    # that note.
    for i in range(0, len(bells)):
        # print (bells[i][2])
        # Does the friendly name in this list match what we're looking for?
        if s == bells[i][2]:
            # Yes! Play the sound.
            bells[i][0].play(loops=0, maxtime=0, fade_ms=0)
            break;
