from jinglefilewalker import *

tweet = "#nustem red winter"

# remove the hastag
tweet = tweet.replace("#nustem ", "")
# lower case it and list is
tweet = tweet.lower()
tweetList = tweet.split()

print(tweetList)

#print(songdict)

B = ['dreaming','of','a','white','christmas']
songLength = len(B)

similars = set(tweetList).intersection(B)
matchLength = len(similars)

print(matchLength/songLength)