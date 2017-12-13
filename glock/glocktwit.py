from twitcreds import *
from twython import TwythonStreamer
from songsearcher import *
import paho.mqtt.client as mqtt

mqttc = mqtt.Client()
mqtt_server = "10.0.1.5"
# mqtt_server = "127.0.0.1"


def message(payload):
    """Abstract out MQTT connection.
    Since it has to be done for each message, wrap it in a function.
    """
    mqttc.connect(mqtt_server, 1883)
    mqttc.publish("orchestra/cue", payload)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'])
            a,b,c = searcher(data['text'])
            print(a, b)
            print("Sending RTTTL file to MQTT")
            message(c)
            print("Complete.")

    def on_error(self, status_code, data):
        print(status_code)

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()

if __name__ == "__main__":
    stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    while True:
        print("Listening to Twitter")
        stream.statuses.filter(track='#copperglock')
        
