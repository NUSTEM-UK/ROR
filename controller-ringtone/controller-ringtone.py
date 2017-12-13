"""Robot Orchestra controller - taking RTTTL ringtone requests from Twitter.

Elements drawn from Pimoroni Piano HAT code:
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
from threading import Timer
import paho.mqtt.client as mqtt # requires `pip install paho-mqtt`
import numpy as np
# from math import log2, pow # Python3 has a log2
from math import log, pow

try:
    pygame.init()
except ImportError:
    exit("This script requires the pygame module\nInstall with: sudo pip install pygame")

BANK = os.path.join(os.path.dirname(__file__), "sounds")

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

mqttc = mqtt.Client()
# mqtt_server = "127.0.0.1"
mqtt_server = "10.0.1.5"


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

def on_connect(self, client, userdata, rc):
    """Connect to MQTT broker & subscribe to cue channel."""
    print("Connected with result code: " + str(rc))
    self.subscribe("orchestra/cue")

def message(topic, payload):
    """Abstract out MQTT connection.

    Since it has to be done for each message, wrap it in a function.
    """
    mqttc.connect(mqtt_server, 1883)
    mqttc.publish("orchestra/" + topic, payload)

def playset(beatset):
    """Sends the current beat to all 8 channels at once."""
    message("playset", beatset)

def on_message(client, userdata, msg):
    """Handle incoming playback cue."""
    notedict = {"C":36, "C#":37, "D":38, "D#":39, "E":40, "F":41, "F#":42, "G":43, "G#":44, "A":45, "A#":46, "B":47}
    channeldict = {"C":0, "C#":0, "D":1, "D#":1, "E":2, "F":3, "F#":3, "G":4, "G#":4, "A":5, "A#":5, "B":6}

    # print("Topic:", msg.topic + '  :  Message: ' + msg.payload)
    print(msg.topic, msg.payload)

    tune = RTTTL(msg.payload)

    for freq, msec in tune.notes():        
        # print(freq, msec)
        if freq != 0.0:
            note, oct = freq_to_note(freq)
            print(note, oct)
            play_beats = list("00000000") # fresh playlist. List so mutable
            play_beats[channeldict[note]] = "1"
            playset(''.join(play_beats)) # Command the orchestra!
            handle_note(notedict[note], oct)
            sleep(msec/1000.0)
        else:
            print('Rest!')
            sleep(msec/1000.0)

    # Make sure the last note plays
    sleep(0.3)
    print(">>> Playback complete!")

load_samples(patches[patch_index])


# tune = RTTTL(songdict['Oh little star of bethlehem'])
# tune = RTTTL(songdict['Jingle Bells'])
# tune = RTTTL(songdict['Frosty the snowman'])
# tune = RTTTL(songdict["I'm dreaming of a white christmas"])
# tune = RTTTL(songdict['Take On Me'])
# tune = RTTTL(songdict['Airwolf Theme'])

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqtt_server, 1883)
client.loop_forever()
