import paho.mqtt.client as mqtt
from time import sleep

mqttc = mqtt.Client()
mqtt_server = "10.0.1.5"

def message(topic, payload):
    mqttc.connect(mqtt_server, 1883)
    mqttc.publish("orchestra/"+topic, payload)

# message("song", "Another song with a long name")
# message("handle", "@fred")
# sleep(1)
# message("song", "Short name")
# message("handle", "@jjsanderson")
# sleep(1)
message("song", "We Wish You a Merry Christmas")
message("handle", "Joe. Always Joe.")
message("cue", "ThePriso:d=4,o=6,b=160:8c#7,8b,2c#.,8b,8a,2b.,8a,g#,8a#,8f#,8d,8c#,f#,d,8c#,8f#,8d,8c#,f#,8c#,8b,c#7,b,a,g#,c#,8e,8c#,d#,8a,8b,c#7,b,a,g#,c#,8e,8c#,8d#,8a,b,2c#7,b,8a,8g#,c#,8e,8c#,d#,8e,8f#,g#.,g#.,g#,8g#,8p,8g#,8f#,8g#,8p,8d#,8c#,8d#,8p,8g#,8f#,8g#,8p,8g#7,8f#7,g#7,8f#7,8e7,f#7,8e7,8d#7,8c#7,8g#,f#,c#,8g#7,8f#7,g#7,8f#7,8e7,f#7,8e7,8d#7,8c#7,8e,b5,2a5")