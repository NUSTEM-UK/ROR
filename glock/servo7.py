from twitcreds import *
from twython import TwythonStreamer, Twython, TwythonError 
from random import randint

tweetList = [
    "@nustemxmas No, please no, don't do this to me!",
    "@nustemxmas My nerves are wrecked, please stop tweeting.",
    "@nustemxmas I hate my life.",
    "@nustemxmas Santa, please stop this madness.",
    "@nustemxmas I have zero job satisfaction.",
    "@nustemxmas Just let me rest, please let me rest.",
    "@nustemxmas I don't think I can take this anymore.",
    "@nustemxmas The bells! The bells! Please stop the bells.",
    "@nustemxmas Do you think I enjoy my job? I wanted to be a fighting robot. And here I am stuck hitting a poorly cut, out-of-tune piece of copper pipe with a chopstick.",
    "@nustemxmas I'm not even I'm tune, I'm flat, I sound horrendous.",
    "@nustemxmas Coffee, I need more coffee."
]

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            if userData['screen_name'] == "ServoSeven":
                continue
            print("Tweet received")
            servoTweet = tweetList[randint(0,len(tweetList))]
            print(servoTweet)
            try:
                photo = open("servo7.gif", 'rb')
                response = SEVENtwitter.upload_media(media=photo)
                SEVENtwitter.update_status(status=servoTweet, media_ids=[response['media_id']])
                print("Upload successful")
                photo.close()
                print("Video closed")
            except TwythonError as e:
                print(e) 

    def on_error(self, status_code, data):
        print(status_code)

SEVENstream = MyStreamer(servoAPP_KEY, servoAPP_SECRET, servoOAUTH_TOKEN, servoOAUTH_TOKEN_SECRET)
SEVENtwitter = Twython(servoAPP_KEY, servoAPP_SECRET,servoOAUTH_TOKEN, servoOAUTH_TOKEN_SECRET)

if __name__ == "__main__":
    while True:
        print("Listening to Twitter")
        #choose your search term wisely - there's a lot of tweets out there
        SEVENstream.statuses.filter(track='@NUSTEMxmas')