#from jinglefilewalker import *
from rttllist import *
# dependency pip3 install fuzzywuzzy
# pip3 install python-Levenshtein - not dependent but removes an annoying warning
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
        accuracy = fuzz.token_set_ratio(tweet,key)
        if accuracy > bestAccuracy:
            bestGuess = key
            bestAccuracy = accuracy
            bestRTTTL = value
    return(bestGuess, bestAccuracy, bestRTTTL)

if __name__ == "__main__":
    tweet = "#nustem walking"
    a,b,c = searcher(tweet)
    print(a,b)
    print(c)