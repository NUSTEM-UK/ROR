"""Test audio playback in Pygame

This has to be run from the /experiments directory for the
paths to work correctly.
"""

import pygame
import signal
from time import sleep

pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.init()
pygame.mixer.init()
sound01 = pygame.mixer.Sound("../piano_pi/sounds/drums/smash.wav")
sound02 = pygame.mixer.Sound("../piano_pi/sounds/piano/39160__jobro__piano-ff-013.wav")

sound01.play()
sleep(1)
sound02.play()
sleep(1)


# Need to pause here to give sound time to play
sleep(1)
# signal.pause()
