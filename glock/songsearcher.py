from jinglefilewalker import *

def searcher(tweet):
    # remove the hastag
    tweet = tweet.replace("#copperglock ", "")
    bestGuess = []
    bestAccuracy = 0
    # lower case it and list is
    tweet = tweet.lower()
    tweetList = tweet.split()
    for key, value in songdict.items():
        songLength = len(value)
        similars = set(tweetList).intersection(value)
        matchLength = len(similars)
        accuracy = matchLength/songLength
        if accuracy > bestAccuracy:
            bestGuess = key
            bestAccuracy = accuracy
    return(bestGuess, bestAccuracy)

if __name__ == "__main__":
    tweet = "#nustem away"
    a,b = searcher(tweet)
    print(a,b)