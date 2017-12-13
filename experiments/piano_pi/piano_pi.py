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
    octave = (h // 12) - 6
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

# tune = RTTTL(songdict["The First Noel"])
# tune = RTTTL(songdict["Hark the Herald Angels Sing"])

# tune = RTTTL(songdict["Frosty the Snowman"])
# tune = RTTTL(songdict["We Wish You a Merry Christmas"])
# tune = RTTTL(songdict["We Wish You a Merry Christmas 2"])
# tune = RTTTL(songdict["Oh Little Town of Bethlehem"])
# tune = RTTTL(songdict["On Ilkley Moor"])
# tune = RTTTL(songdict["The 12 Days of Christmas"])
# tune = RTTTL(songdict["Rudolph the Red-Nosed Reindeer"])
# tune = RTTTL(songdict["Santa Claus is Coming To Town"])
# tune = RTTTL(songdict["Walking in the Air"])
# tune = RTTTL(songdict["Take On Me"])
# tune = RTTTL(songdict["Airwolf Theme"])
# tune = RTTTL(songdict["All I Want for Christmas"])
# tune = RTTTL(songdict["Do They Know It's Christmas"])
# tune = RTTTL(songdict["Amazing Grace"])
# tune = RTTTL(songdict["Deck the Halls"])
# tune = RTTTL(songdict["God Rest Ye Merry Gentlemen"])
# tune = RTTTL(songdict["Jingle Bells"])
# tune = RTTTL(songdict["Joy to the World"])
# tune = RTTTL(songdict["Last Christmas"])
# tune = RTTTL(songdict["Last Christmas 2"])
# tune = RTTTL(songdict["Last Christmas 3"])
# tune = RTTTL(songdict["Last Christmas 5"])
# tune = RTTTL(songdict["Let it Snow"])
# tune = RTTTL(songdict["Oh Christmas Tree"])
# tune = RTTTL(songdict["Oh Come All Ye Faithful"])
# tune = RTTTL(songdict["Silent Night"])
# tune = RTTTL(songdict["We Three Kings"])
# tune = RTTTL(songdict["Winter Wonderland"])
# tune = RTTTL(songdict["Away in a Manger"])
# tune = RTTTL(songdict["Good King Wenceslas"])
# tune = RTTTL(songdict["Jingle Bells Rock"])
# tune = RTTTL(songdict["Jingle Bells"])
# tune = RTTTL(songdict["Little Drummer Boy"])
# tune = RTTTL(songdict["Oh Christmas Tree"])
# tune = RTTTL(songdict["I Wish it Could be Christmas Every Day"])
# tune = RTTTL(songdict["I Wish it Could be Christmas Every Day 2"])
# tune = RTTTL(songdict["It's Beginning to Look a Lot Like Christmas"])
# tune = RTTTL(songdict["So This is Christmas"])
# tune = RTTTL(songdict["Have Yourself a Merry Little Christmas"])
# tune = RTTTL(songdict["So Here it is Merry Christmas"])
# tune = RTTTL(songdict["The Prisoner"])


string = "Wonderfu:d=4,o=6,b=160:16b5,16p,8b5,8p,8c_,8d_.,1p,p,16p,16b5,16p,8b5,8p,8c_,8d_.,1p,p,16p,16b5,16p,8b5,8p,8c_,8d_,1p,p,8p,16b5,16p,8b5,8p,8c_,8d_.,2p,p,8p,16p,d_,p,c_.,8p,e.,8p,d_,8p,8d_,f_,8e,8d_,8b5,8p,8b5,8p,2b5,2p,d_,p,c_.,8p,e.,8p,d_,8p,8d_,f_,8e,8d_,8b5,8p,8b5,8p,2b5"
tune = RTTTL(string)




for freq, msec in tune.notes():
    print(freq, msec)
    if freq != 0.0:
        note, oct = freq_to_note(freq)
        print(note, oct)
        play_beats = list("00000000")
        play_beats[channeldict[note]] = "1"
        print(''.join(play_beats))
        handle_note(notedict[note], oct)
        sleep(msec/1000.0)
    else:
        sleep(msec/1000.0)

# Make sure the last note plays
sleep(0.3)
