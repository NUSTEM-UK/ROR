# import all the modules needed for the mettalophone to run
from twitcreds import *     # this file stores our Twitter credentials
from twython import TwythonStreamer, Twython, TwythonError    # here we import Twython which allows us to talk to twitter
from songsearcher import *  # this module takes a tweet and matches it with a song
import paho.mqtt.client as mqtt # paho sends and receives messages over MQTT on our internal network
from rtttl import RTTTL # this model helps us get the duration of a song
from time import sleep # bedtime
from videos import *    # import link sto all the video files
from rttllist import *

# set up the variables for the MQTT server
mqttc = mqtt.Client()
mqtt_server = "10.0.1.5"
# mqtt_server = "127.0.0.1"

# this function sends data to the MQTT
def message(topic, payload):
    mqttc.connect(mqtt_server, 1883)
    mqttc.publish(topic, payload)

# this is the Twython streamer, it will listen for Tweets on a hashtag and act accordingly
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            #print(data)
            #print(data['text'])
            userData = data['user']
            print(userData['screen_name'])
            #print(data['text'])

            # use the searcher module to match the tweet to a song in our library
            a,b,c = searcher(data['text'])
            #print(a, b)
            #print("Checking song duration:")

            # here we check the duration of the song
            tune = RTTTL(c)
            totalTime = 0
            for freq, msec in tune.notes():
                totalTime += msec

            #print(totalTime)
            print("Sending RTTTL file to MQTT")

            # now send the various bits of data: twitter user, song name and RTTTL file to MQTT
            
            message("orchestra/song", a)
            sleep(0.2)
            message("orchestra/handle", "@"+userData['screen_name'])
            sleep(0.2)
            message("orchestra/cue", c)
            print("sending successful")

            #check to see if we have the video
            if a in videos:
                vidURL = videos[a]
            else:
                vidURL = ""
            # create a pleasant thank you tweet and send back
            tweet = "@" + userData['screen_name'] + " Thanks for your song request. We're " + str(b) + "%" + " sure you requested: " + a + ". Merry Christmas from NUSTEM. " + vidURL
            #tweet = "@" + userData['screen_name'] + " Thanks for your song request! We're now playing: " + a +  ". Merry Christmas from NUSTEM. " + vidURL
            print(tweet)
            if a in egg:
                try:
                    print("Easter Egg!")
                    photo = open(egg[a], 'rb')
                    response = twitter.upload_media(media=photo)
                    twitter.update_status(status=tweet, media_ids=[response['media_id']])
                    print("Upload successful")
                    photo.close()
                    print("Video closed")
                except TwythonError as e:
                    print(e) 
            else:
                try:
                    twitter.update_status(status=tweet, in_reply_to_status_id=str(data['id']))  
                    print("Tweet sent succesfully")
                except TwythonError as e:
                    print(e)          

    def on_error(self, status_code, data):
        print(status_code)
        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()

# if __name__ == "__main__" means this code will only run if this is the main python code (not imported as a module)
if __name__ == "__main__":
    #connect to the stream and twitter
    stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    while True:
        print("Listening to Twitter")
        #choose your search term wisely - there's a lot of tweets out there
        stream.statuses.filter(track='@NUSTEMxmas')
        #stream.user()
        
