#!/usr/bin/python

# References
# -----------
# 1. An Introduction to Text Mining using Twitter Streaming API and Python
#    http://adilmoujahid.com/posts/2014/07/twitter-analytics/

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import api
import json
import pandas as pd

#Variables that contains the user credentials to access Twitter API 
access_token = # generated from twitter account
access_token_secret = # generated from twitter account
consumer_key = # generated from twitter account
consumer_secret = # generated from twitter account

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
#        print json.loads(data)#, sort_keys=True, indent=4, separators=(',', ':'))
        print json.dumps(json.loads(data), sort_keys=True, indent=4, separators=(',', ':'))
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
