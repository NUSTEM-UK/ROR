"""Listen for playset messages over MQTT, and route them out to servos.

See PinFactory documentation here: 
http://gpiozero.readthedocs.io/en/stable/api_pins.html#changing-the-pin-factory

(need to use pigpio factory for better PWM handling)
"""
import paho.mqtt.client as mqtt
from time import sleep
from gpiozero import Servo

myservo = [Servo(27), Servo(22), Servo(10), Servo(11),
           Servo(6), Servo(13), Servo(19), Servo(26)]


def on_connect(client, userdata, rc):
    """Connect to MQTT broker & subscribe to playset channel."""
    print("Connected with result code: " + str(rc))
    client.subscribe("orchestra/playset")


def on_message(client, userdata, msg):
    """Handle incoming messages."""
    print("Topic:", msg.topic + '  :  Message: ' + msg.payload)
    for i, beat in enumerate(msg.payload):
        # print(i, beat)
        if beat == "1":
            print(i, ": BONG!")
            myservo[i].max()
        else:
            print(i, ": PISH!")
            myservo[i].min()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# client.connect('10.0.1.5', 1883)
client.connect('127.0.0.1', 1883)
client.loop_forever()
