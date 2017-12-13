"""Software piano test.

Pulled mostly from Pimoroni Piano HAT code:
https://github.com/pimoroni/Piano-HAT/blob/master/examples/simple-piano.py
"""

import glob
import os
import re
import pygame
from time import sleep
from sys import exit
from rtttl import RTTTL
from rttllist import songdict
# from math import log2, pow # Python3 has a log2
from math import log, pow

try:
    pygame.init()
except ImportError:
    exit("This script requires the pygame module\nInstall with: sudo pip install pygame")

BANK = os.path.join(os.path.dirname(__file__), "../piano_pi/sounds")

NOTE_OFFSET = 0
FILETYPES = ['*.wav', '*.ogg']
samples = []
files = []
octave = 0
octaves = 0

# Tuning, and constants for freq-to-note conversion
A4 = 440
C0 = A4*pow(2, -4.75)
name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

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
    channel = channel + (12 * octave) + NOTE_OFFSET
    if channel < len(samples):
        # print('Playing Sound: {}'.format(files[channel]))
        print('Playing sound: {}'.format(channel))
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


def freq_to_note(freq):
    """Outputs note and octave for input frequency.

    Based on https://www.johndcook.com/blog/2016/02/10/musical-pitch-notation/
    by John D. Cook
    """
    # h = round(12*log2(freq/C0)) # Python3 only
    h = round(12*(log(freq/C0)/log(2)))
    print(">>>")
    print(h)
    octave = (h // 12) - 5
    n = h % 12
    return name[int(n)], int(octave)

load_samples(patches[patch_index])

# Old test code I haven't deleted yet.
# This really should have been in /experiments, but there you go.

# scale_up(8, 0.1)
# scale_down(8, 0.1)
# sleep(1)

# handle_note(36, 1)
# sleep(1)
# handle_note(48, 0)
# sleep(1)

# scale = [36, 38, 40, 41, 43, 45, 47, 48]
# for note in scale:
#     handle_note(note-1, 0)
#     sleep(0.3)
# sleep(1)
# scale2 = [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
# for note in scale2:
#     handle_note(note-1, 0)
#     sleep(0.3)

# sleep(1)
# scale3 = {"C":36, "D":38, "E":40, "F":41, "G":43, "A":45, "B":47, "C2":48}
# for note in "C,D,E,F,G,A,B,C2".split(","):
#     print("Playing {}".format(note))
#     handle_note(scale3[note], 0)
#     sleep(0.3)

notedict = {"C":36, "C#":37, "D":38, "D#":39, "E":40, "F":41, "F#":42, "G":43, "G#":44, "A":45, "A#":46, "B":47}
channeldict = {"C":0, "C#":0, "D":1, "D#":1, "E":2, "F":3, "F#":3, "G":4, "G#":4, "A":5, "A#":5, "B":6}

tune = RTTTL(songdict['Oh little star of bethlehem'])
# tune = RTTTL(songdict['Jingle Bells'])
# tune = RTTTL(songdict['Frosty the snowman'])
# tune = RTTTL(songdict["I'm dreaming of a white christmas"])
for freq, msec in tune.notes():
    print(freq, msec)
    if freq != 0.0:
        note, oct = freq_to_note(freq)
        print(note, oct)
        handle_note(notedict[note], oct)
        sleep(msec/1000.0)
    else:
        sleep(msec/1000.0)

# Make sure the last note plays
sleep(0.3)
