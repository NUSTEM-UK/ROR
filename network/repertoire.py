"""Command the system directly for testing purposes.

Steps through the song list and commands playback of each tune. For testing
and video purposes.
"""

import paho.mqtt.client as mqtt
from time import sleep
from rtttl import RTTTL
from rttllist import *

mqttc = mqtt.Client()
mqtt_server = "10.0.1.5"

def message(topic, payload):
    mqttc.connect(mqtt_server, 1883)
    mqttc.publish("orchestra/"+topic, payload)

def get_duration(rtttl_melody):
    duration = 0
    for freq, msec in rtttl_melody.notes():
        duration += msec
    return duration

print(">>> START")
sleep(2)

for song, cue in songdict.items():
    tune = RTTTL(cue)
    duration = get_duration(tune)
    # print(song, duration)
    print(song)
    message("cue", cue)
    sleep((duration/1000)+2) # Wait until it's finished
