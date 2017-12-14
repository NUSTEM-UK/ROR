from rttllist import *
from bigrtttl import *
# dependency pip3 install fuzzywuzzy
# pip3 install python-Levenshtein - not dependent but removes an annoying warning
# fuzzywuzzy does our matching
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def searcher(tweet):
    # remove the hastag
    tweet = tweet.replace("#nustemplay", "")
    bestGuess = []
    bestAccuracy = 0
    # lower case it and list is
    tweet = tweet.lower()
    # if the tweet contains #easteregg
    if "#easteregg" in tweet:
        print("EASTER EGG")
        tweet = tweet.replace("#easteregg", "")
 #   tweetList = tweet.split()
        for key, value in songdictEgg.items():
            accuracy = fuzz.token_set_ratio(tweet,key)
            if accuracy > bestAccuracy:
                bestGuess = key
                bestAccuracy = accuracy
                bestRTTTL = value
    else:
        for key, value in songdict.items():
            accuracy = fuzz.token_set_ratio(tweet,key)
            if accuracy > bestAccuracy:
                bestGuess = key
                bestAccuracy = accuracy
                bestRTTTL = value
    return(bestGuess, bestAccuracy, bestRTTTL)

# if __name__ == "__main__" means this code will only run if this is the main python code (not imported as a module)
if __name__ == "__main__":
    tweet = "#nustem walking"
    a,b,c = searcher(tweet)
    print(a,b)
    print(c)