"""Command the system directly for testing purposes.

Basic MQTT messaging client, allows broadcast of commands to different elements
of the system. Comment out the bits you don't want to test!
"""

import paho.mqtt.client as mqtt
from time import sleep

mqttc = mqtt.Client()
mqtt_server = "10.0.1.5"

def message(topic, payload):
    mqttc.connect(mqtt_server, 1883)
    mqttc.publish("orchestra/"+topic, payload)

# Test long and short strings to check line padding on Displayotron HAT
# message("song", "Another song with a long name")
# message("handle", "@fred")
# sleep(1)
# message("song", "Short name")
# message("handle", "@jjsanderson")
# sleep(1)

# For debugging/testing Displayotron HAT output.
message("song", "An E.")
message("handle", "For Joe. Also Luke.")

# For debugging song playback and testing RTTTL transcripts
message("cue", "DeckTheH:d=8,o=6,b=140:4g.,f,4e,4d,4c,4d,4e,4c,d,e,f,d,4e.,d,4c,4b5,2c,4g.,f,4e,4d,4c,4d,e,b5,c,g5,d,e,f,d,4e,c,d,c,a5,b5,f5,2c,4d.,e,4f,4d,4e.,f,4g,4d,e,f#,g,d5,a,b,4c7,4b,a,c,g,a5,g5,f5,4g.,f,4e,4d,4c,4d,4e,4c,a,a,a,a,4g.,f,4e,4d,2")

# For hammer alignment - uncomment individually
# message("playset", "10000000") # C
# message("playset", "01000000") # D
# message("playset", "00100000") # E
# message("playset", "00010000") # F
# message("playset", "00001000") # G
# message("playset", "00000100") # A
# message("playset", "00000010") # B
# message("playset", "00000001") # C (top, never played)

# Test multiple rapid hits
# (the hammers tend to get stuck, so this allows some fine-tuning)
# for i in range(5):
#     message("playset", "11111111") # D
#     sleep(0.2)

# Test scales up and town, multiple times
# for i in range(2):
#     delay = 0.2
#     message("playset", "10000000")
#     sleep(delay)
#     message("playset", "01000000")
#     sleep(delay)
#     message("playset", "00100000")
#     sleep(delay)
#     message("playset", "00010000")
#     sleep(delay)
#     message("playset", "00001000")
#     sleep(delay)
#     message("playset", "00000100")
#     sleep(delay)
#     message("playset", "00000010")
#     sleep(delay)
#     message("playset", "00000001")
#     sleep(delay*2)
#     message("playset", "00000001")
#     sleep(delay)
#     message("playset", "00000010")
#     sleep(delay)
#     message("playset", "00000100")
#     sleep(delay)
#     message("playset", "00001000")
#     sleep(delay)
#     message("playset", "00010000")
#     sleep(delay)
#     message("playset", "00100000")
#     sleep(delay)
#     message("playset", "01000000")
#     sleep(delay)
#     message("playset", "10000000")
#     sleep(delay*2)
