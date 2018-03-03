#!/usr/bin/python

import tweepy_setup as ts
import json
import tweepy
import pandas
#from codecs import encode
import tweets_streamer
import operator
import time
import pickle
import tweepy_setup
#print json.dumps(result, sort_keys=True, indent=4, separators=(',', ':'))

u=tweepy_setup.api.get_user(755254730322870274)
print u
#print json.dumps(json.load(u))
