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

# Returns the list of currently trending hashtags
def get_trending_hashtags(api):
    trending_list=[]
    trends=api.trends_place(1)
    for trend in trends[0][u'trends']:
        trending_list.append(trend[u'name'])
    return trending_list

# Stream, filter and return 'limit' number of tweets
def get_filtered_tweets(auth, trending_list, limit):
    filtered_tweets=tweets_streamer.stream_tweets(auth, trending_list, limit)
    return filtered_tweets

# Finds 'limit' number of users with maximum followers
def get_maximum_followed(filtered_tweets, limit):
    maximum_followed=[]
    for tweet in filtered_tweets:
#        print tweet.keys()
        try:
            user=tweet['user']
            print "User ID: "+user['id_str']
            print "Followers Count: "+str(user['followers_count'])
            maximum_followed.append(user)
        except KeyError as e:
            print "Key error: ",
            print e
    # Sort the list according to maximum followed
    maximum_followed=sorted(maximum_followed, key=operator.itemgetter('followers_count'), reverse=True)
    # Return a sublist of the required length
    return maximum_followed[0:limit]

# Finds 'limit' number of followers for the given user
def get_followers(api, auser, limit):
    followers=[]
    if type(auser)==tweepy.models.User:
        user_id=auser.id
    else:
        user_id=auser['id']
    for page in tweepy.Cursor(api.followers, id=user_id).pages():
        followers.extend(page)
        if len(followers)>=limit:
            break
#        time.sleep(60)
    # Sort the list according to maximum followed
    followers=sorted(followers, key=lambda x: x.followers_count, reverse=True)
    return followers[0:limit]

# Get users data set
def get_users_data_set():
    users_data_set=None # Decide its type
    return users_data_set

# Checks the rate limit status and quits the program
def check_rate_limit_status():
    rate_limit_status=api.rate_limit_status()
    l.log("Rate limit status: ")
    l.log(json.dumps(rate_limit_status, sort_keys=True, indent=4, separators=(',', ':')))
    quit()

if __name__=='__main__':

    quit() # for testing
    
    # Create local logger
    l=LocalLogger()
    # Get trending hashtags
    trending_hashtags=get_trending_hashtags(ts.api)
    l.log("Trending hashtags obtained.")
    # Get filtered tweets
    filtered_tweets=get_filtered_tweets(ts.auth, trending_hashtags, 50)
    l.log("Filtered tweets obtained.")
    # Get users with maximum followers; keys- user->id,followers_count; but how do you find followers?
    maximum_followed=get_maximum_followed(filtered_tweets, 10)
    l.log("Users with maximum followers obtained.")
    # Get followers of these users
    for auser in maximum_followed:
        followers=get_followers(ts.api, auser, 100)
        fname='followers_'+str(auser['id'])+'.txt'
        f=open(fname, 'w')
        pickle.dump(followers, f)
        f.close()
        print "User ID: ",
        print auser['id']
        print "Followers: ",
        print len(followers)
#    print maximum_followed
