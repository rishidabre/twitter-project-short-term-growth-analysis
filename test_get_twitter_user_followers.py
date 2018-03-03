#!/usr/bin/python

import json
import tweepy

# The consumer secret is an example and will not work for real requests
# To register an app visit https://dev.twitter.com/apps/new
CONSUMER_KEY = # generated from twitter account
CONSUMER_SECRET = # generated from twitter account
ACCESS_TOKEN = # generated from twitter account
ACCESS_TOKEN_SECRET = # generated from twitter account

#print json.dumps(result, sort_keys=True, indent=4, separators=(',', ':'))

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
u=api.get_user(118245982)
#print json.dumps(json.loads(u))
#print u.followers
user_id=u.id
limit=100
followers=[]
for page in tweepy.Cursor(api.followers, id=user_id).pages():
    followers.extend(page)
    if len(followers)>=limit:
        break
#        time.sleep(60)
print len(followers)
