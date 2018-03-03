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

#print json.dumps(result, sort_keys=True, indent=4, separators=(',', ':'))

#u=api.get_user(<some user id>)
#print json.dumps(json.loads(u))
#print u.screen_name

# A barebone logger printing to stdout
class LocalLogger:

    # Print message to console
    def log(self, msg):
        print msg

# Finds 'limit' number of followers for the given user
def get_followers(api, auser, limit):
    followers=[]
    if type(auser)==tweepy.models.User:
        user_id=auser.id
    else:
        user_id=auser
    for page in tweepy.Cursor(api.followers, id=user_id).pages():
        followers.extend(page)
        if len(followers)>=limit:
            break
#        time.sleep(60)
    # Sort the list according to maximum followed
    followers=sorted(followers, key=lambda x: x.followers_count, reverse=True)
    return followers[0:limit]

if __name__=='__main__':

    # Create local logger
    l=LocalLogger()
    # Get users for the following IDs
    maximum_followed=[118245982, 184915348, 2832607445, 3345681971, 433715354] # maxmimum followed users (from randomly obtained list)
    # Get followers of these users
    for auser in maximum_followed:
        followers=get_followers(ts.api, auser, 40)
        fname='followers_'+str(auser)+'_trace_2.txt'
        f=open(fname, 'w')
        pickle.dump(followers, f)
        f.close()
        print "User ID: ",
        print auser
        print "Followers: ",
        print len(followers)
#    print maximum_followed
