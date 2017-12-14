"""Command the system directly for testing purposes.

Basic MQTT messaging client, allows broadcast of commands to different elements
of the system. Comment out the 
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
message("cue", "rickastley:d=4,o=5,b=120:8f,a#3,g,8c4,8c,8c4,8g,a3,a,8d4,16c6,16a#,8a,8f,a#3,g,8c4,8c,8c4,8a2,a3,d3,16c,16c,16d,16f,16d4,16f,8f,a#3,g,8c4,8c,8c4,8g,a3,a,8d4,16c6,16a#,8a,8f,a#3,g,8c4,8c,8c4,8e,8f,8f,8a3,d4,16f,8f,16f,8a#2,8f3,8d,8e,8f,8f,8g,8e.,16d,c,8c4,c4,b3,8a#2,8d,8d,8e,8f,8d,8a#3,8c,16c6,8p,16p,8c6,8g,8c7,8g6,8c8,8g7,8a#2,8d,8d,8e,8f,8d,8f,8g,8c4,8e,8d,8c,c4,b3,8a#2,8d,8d,8e,8f,8d,c,8g,8g,8g,8a,g,b3,8f,8a#3,8a#2,8a#3,8a#2,8g,8a,8f,8g,8g,8g,8a,8g,8c4,8c,8c4,8a#2,8a#3,8a#2,8a#3,8d,8e,8f,8d,16c4,16p,8g,8a,g.,16c,16d,16f,16d,16a.,16p,32p,8a,16p,g.,16c,16d,16f,16d,16g.,16p,32p,8g,16p,8f.,16e,8d,16c,16d,16f,16d,f,8g,8e.,16d,8c,8c4,8c,8g,8p,2f,16c,16d,16f,16d,16a.,16p,32p,8a,16p,g.,16c,16d,16f,16d,c6,8e,8f.,16e,8d,16c,16d,16f,16d,f,8g,8e.,16d,8c,8c4,8c,8g,8p,2f")

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
