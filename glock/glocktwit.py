from twitcreds import *
from twython import TwythonStreamer, Twython
from songsearcher import *
import paho.mqtt.client as mqtt
from rtttl import RTTTL
from time import sleep

mqttc = mqtt.Client()
mqtt_server = "10.0.1.5"
# mqtt_server = "127.0.0.1"


def message(topic, payload):
    """Abstract out MQTT connection.
    Since it has to be done for each message, wrap it in a function.
    """
    mqttc.connect(mqtt_server, 1883)
    mqttc.publish(topic, payload) #"orchestra/cue"

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            #print(data)
            #print(data['text'])
            userData = data['user']
            print(type(userData))
            print(userData['screen_name'])
            
            a,b,c = searcher(data['text'])
            print(a, b)
            print("Checking song duration:")
            tune = RTTTL(c)
            totalTime = 0
            for freq, msec in tune.notes():
                totalTime += msec
            print(totalTime)
            print("Sending RTTTL file to MQTT")
            message("orchestra/song", a)
            time.sleep(0.2)
            message("orchestra/handle", "@"+userData['screen_name'])
            time.sleep(0.2)
            message("orchestra/cue", c)
            tweet = "@" + userData['screen_name'] + " Thanks for your song request! We're now playing: " + a +  ". Merry Christmas from @nustem_uk"
            print(tweet)
            twitter.update_status(status=tweet)


    def on_error(self, status_code, data):
        print(status_code)

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()

if __name__ == "__main__":
    stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    while True:
        print("Listening to Twitter")
        stream.statuses.filter(track='#copperglock')
        
