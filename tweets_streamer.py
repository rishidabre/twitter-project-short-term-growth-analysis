#!/usr/bin/python

# References
# -----------
# 1. An Introduction to Text Mining using Twitter Streaming API and Python
#    http://adilmoujahid.com/posts/2014/07/twitter-analytics/

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import Stream
import json

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    data_set=[]

    def __init__(self, limit):
        self.limit=limit
        return
    
    def on_data(self, data):
#        print json.dumps(json.loads(data), sort_keys=True, indent=4, separators=(',', ':'))
        i=len(self.data_set)
        if i<self.limit:
            print "Filtered %s of %s"%(i+1,str(self.limit))
            self.data_set.append(json.loads(data))
            return True
        else:
            # Disconnect stream
            print "Stream disconnected"
            return False

    def on_error(self, status):
        print status


# Streams up to 'limit' number of tweets according to given filter
def stream_tweets(auth, filters, limit):
    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener(limit)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=filters)

    # Return the streamed data
    return l.data_set
