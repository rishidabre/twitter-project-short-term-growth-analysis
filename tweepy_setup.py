#!/usr/bin/python

import tweepy

# The consumer secret is an example and will not work for real requests
# To register an app visit https://dev.twitter.com/apps/new
CONSUMER_KEY = # generated from twitter account
CONSUMER_SECRET = # generated from twitter account
ACCESS_TOKEN = # generated from twitter account
ACCESS_TOKEN_SECRET = # generated from twitter account

# Create OAuth authentication handler and set access token
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
print "OAuth handler created."
# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
print "API object created."
