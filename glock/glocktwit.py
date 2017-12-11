from twitcreds import *
from twython import TwythonStreamer
from songsearcher import *

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'])
            a,b = searcher(data['text'])
            print(a, b)

    def on_error(self, status_code, data):
        print(status_code)

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        self.disconnect()

stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

while True:
    stream.statuses.filter(track='#copperglock')