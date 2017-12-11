from jinglefilewalker import *
# dependency pip3 install fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def searcher(tweet):
    # remove the hastag
    tweet = tweet.replace("#copperglock ", "")
    bestGuess = []
    bestAccuracy = 0
    # lower case it and list is
    tweet = tweet.lower()
 #   tweetList = tweet.split()
    for key, value in songdict.items():
        #songLength = len(value)
        #similars = set(tweetList).intersection(value)
        #matchLength = len(similars)
        #accuracy = matchLength/songLength
        accuracy = fuzz.partial_ratio(tweet,value)
        if accuracy > bestAccuracy:
            bestGuess = key
            bestAccuracy = accuracy
    return(bestGuess, bestAccuracy)

if __name__ == "__main__":
    tweet = "#nustem all i want christmas"
    a,b = searcher(tweet)
    print(a,b)