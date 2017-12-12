"""Software piano test.

Pulled mostly from Pimoroni Piano HAT code:
https://github.com/pimoroni/Piano-HAT/blob/master/examples/simple-piano.py
"""

import glob
import os
import re
import pygame
import signal
from time import sleep
from sys import exit

try:
    pygame.init()
except ImportError:
    exit("This script requires the pygame module\nInstall with: sudo pip install pygame")

BANK = os.path.join(os.path.dirname(__file__), "../piano_pi/sounds")

NOTE_OFFSET = 3
FILETYPES = ['*.wav', '*.ogg']
samples = []
files = []
octave = 0
octaves = 0

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.mixer.set_num_channels(256)

patches = glob.glob(os.path.join(BANK, '*'))
print(patches)
patch_index = 0

if len(patches) == 0:
    exit("Couldn't find any .wav files in {}".format(BANK))


def natural_sort_key(s, _nsre=re.compile('([0-9]+)')):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(_nsre, s)]


def load_samples(patch):
    global samples, files, octave, octaves
    files = []
    print('Loading samples from: {}'.format(patch))
    for filetype in FILETYPES:
        files.extend(glob.glob(os.path.join(patch, filetype)))
    files.sort(key=natural_sort_key)
    octaves = len(files) / 12
    samples = [pygame.mixer.Sound(sample) for sample in files]
    octave = int(octaves / 2)


def handle_note(channel, octave):
    # channel = channel + (12 * octave) + NOTE_OFFSET
    channel = channel + (12 * octave) + NOTE_OFFSET
    if channel < len(samples):
        print('Playing Sound: {}'.format(files[channel]))
        samples[channel].play(loops=0)
    else:
        print('Note out of bounds')


def handle_octave_up():
    global octave
    if octave < octaves:
        octave += 1
        print('Selected Octave: {}'.format(octave))


def handle_octave_down():
    global octave
    if octave > 0:
        octave -= 1
        print('Selected Octave: {}'.format(octave))


def scale_up(notes, delay):
    global octave
    for note in range(notes):
        handle_note(note, octave)
        sleep(delay)


def scale_down(notes, delay):
    global octave
    for note in range(notes):
        handle_note(notes-note, octave)
        sleep(delay)

load_samples(patches[patch_index])

scale_up(8, 0.1)
scale_down(8, 0.1)
sleep(1)
handle_note(30, 2)
sleep(0.5)
handle_note(30, 3)
sleep(0.5)
handle_note(30, -2)



# Need to pause here to give sound time to play
sleep(1)
# signal.pause()
