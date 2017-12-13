import paho.mqtt.client as mqtt
from time import sleep

mqttc = mqtt.Client()
mqtt_server = "10.0.1.5"

def message(topic, payload):
    mqttc.connect(mqtt_server, 1883)
    mqttc.publish("orchestra/"+topic, payload)

message("song", "Another song with a long name")
message("handle", "@fred")
sleep(1)
message("song", "Short name")
message("handle", "@jjsanderson")
sleep(1)
message("song", "Let it Snow")
message("handle", "Carol")
message("cue", "letitsnow:d=4,o=6,b=140:c.,8a_5,8p,8a5,8p,8g5,f5,c5,p,8c5,8c5,g5,p,8g5,g5,f5,e5,c5,p,8d5,8d5,8d,8c,8p,8a_5,8p,8a5,8p,2g5,8p,p,8e,8d,c,8c,8a_5,a5,8a5,8g5,2f5,2p,c.,8a_5,8p,8a5,8p,8g5,f5,c5,p,8c5,8c5,g5,8p,8g5,g5,f5,e5,c5,p,8d5,8d5,8d,8c,8p,8a_5,8p,8a5,8p,2g5,8p,p,8e,8d,c,8c,8a_5,a5,8a5,8g5,2f5")