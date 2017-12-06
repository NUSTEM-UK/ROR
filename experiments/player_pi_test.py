"""Listen for playset messages over MQTT, and route them out to servos.

"""
import paho.mqtt.client as mqtt


def on_connect(client, userdata, rc):
    """Connect to MQTT broker."""
    print("Connected with result code: " + str(rc))
    client.subscribe("#")


def on_message(client, userdata, msg):
    """Output diagnostic when message sent via broker."""
    print("Topic:", msg.topic + '  :  Message: ' + msg.payload)
    for i, beat in enumerate(msg.payload):
        # print(i, beat)
        if beat == "1":
            print("BONG!")
        else:
            print("PISH!")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# client.connect('10.0.1.5', 1883)
client.connect('127.0.0.1', 1883)
client.loop_forever()
