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
import dothat.backlight as backlight
import dothat.lcd as lcd

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

# Display-o-Tron setup
lcd.clear()
# lcd.set_contrast(30)
lcd.write("SYSTEM START")
backlight.graph_off()


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
    self.subscribe("orchestra/song")
    self.subscribe("orchestra/handle")

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
    """Handle incoming messages."""
    # print("Topic:", msg.topic + '  :  Message: ' + msg.payload)
    print(str(msg.topic), str(msg.payload))
    
    if str(msg.topic) == "orchestra/cue":
        lcd.set_cursor_position(0,0)
        lcd.write("Now playing:".ljust(16))

        """Handle incoming playback cue."""
        notedict = {"C":36, "C#":37, "D":38, "D#":39, "E":40, "F":41, "F#":42, "G":43, "G#":44, "A":45, "A#":46, "B":47}
        channeldict = {"C":0, "C#":0, "D":1, "D#":1, "E":2, "F":3, "F#":3, "G":4, "G#":4, "A":5, "A#":5, "B":6}
        
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
        lcd.clear()
        lcd.set_cursor_position(0,0)
        lcd.write("POISED READY")

    elif str(msg.topic) == "orchestra/song":
        print("Song title received")
        lcd.set_cursor_position(0,1)
        lcd.write(str(msg.payload[:16]).ljust(16))

    elif str(msg.topic) == "orchestra/handle":
        lcd.set_cursor_position(0,2)
        lcd.write("For: " + str(msg.payload[:11]).ljust(11))
   
    else:
        print("Well, that didn't work")

load_samples(patches[patch_index])

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqtt_server, 1883)
client.loop_forever()
