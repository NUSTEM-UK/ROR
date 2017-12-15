# Using Twython: an NUSTEM guide
## Introduction
This project using a python package called [Twython](https://twython.readthedocs.io/en/latest/index.html#) to read and write tweets. This guide below will help you set up Twython on your Raspberry Pi and enable to send and recevie tweets. It's worth checking the **How to not get blocked** section at the bottom as that's where I've had most trouble with Twitter.
## Installing Twython
Open up your terminal and type `sudo pip install twython`, if you are using python3 you may also need to `sudo pip3 instal twython`. If this doesn't work on your system, try `sudo easy_install twython`
## Creating a Twitter App
Next you need to head over to Twitter, we need various security keys to make out python script work. Login using your account and then head to https://apps.twitter.com. Click `Create New App` and fill in the details on the next page. You can choose the name (it needs to be unique) and you can ignore the callback url bit. Check the 'I have read...' box and create your app.

On you new page you need to find the `Keys and access tokens` tab and make a note of:
* Consumer Key (API Key)
* Consumer Secret (API Secret)

Then click to get your access tokens and make a note of:
* Access Token
* Access Token Secret

You now have everything you need. 

## Reading a stream of Tweets
### Step 1 - create your key file
Create a new python file and call it `twitcreds.py`. Fill it with your access keys like this:
```
APP_KEY = '???'
APP_SECRET = '???'
OAUTH_TOKEN = '???'
OAUTH_TOKEN_SECRET = '???'
```
### Step 2 - create your python file and import Twython and your access keys
Create a new python file and cal it `twitterApp.py` (you can choose your own name). Import Twython and your access keys:
```
from twython import TwythonStreamer, Twython, TwythonError
from twitcreds.py import *
```
### Step 3 - create your Streamer class
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            #print(data)
            #print(data['text'])
## Tweeting a user
## How to not get blocked
You can work out if you've been blocked by heading to your twitter app - https://apps.twitter.com. If you've been blocked, there'll be a red bar next to your app. Easiest thing to down now is to create a brand new app and record the new keys. The alternative is to request an unblocking which can take days and may not be successful.  