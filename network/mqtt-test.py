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
message("song", "Jingle Bells")
message("handle", "Joe. Always Joe.")
message("cue", "AllIWant:d=4,o=6,b=160:c5,e5,g5,8b5,c,b.5,8a5,g.5,d,c,8c,b5,c,b5,8a5,2g5,a5,c,8d,e,d,c,a.5,f5,8g#5,c.,8d,d#,d,a#5,g#.5,c,d,b5,8c,a5,b5,2g#5,c,d,b5,8c,a5,b5,2g#5,g5,a5,8c,g,f,8g,2f,e,d,c,a5,g#5,2d,e,8d.,2c.")