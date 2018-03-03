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
from datetime import date
from sys import argv

cur_date=date.today().__str__()

#print json.dumps(result, sort_keys=True, indent=4, separators=(',', ':'))

#u=api.get_user(<some_user_id>)
#print json.dumps(json.loads(u))
#print u.screen_name

# Returns the list of currently trending hashtags
def get_trending_hashtags(api):
    trending_list=[]
    trends=api.trends_place(1)
    for trend in trends[0][u'trends']:
        trending_list.append(trend[u'name'])
    with open("trending_tags_%s.txt"%cur_date,'w') as f:
        pickle.dump(trending_list,f)
    return trending_list

# Stream, filter and return 'limit' number of tweets
def get_filtered_tweets(auth, trending_list, limit):
    filtered_tweets=tweets_streamer.stream_tweets(auth, trending_list, limit)
    with open("filtered_tweets_%s.txt"%cur_date,'w') as f:
        pickle.dump(filtered_tweets,f)
    return filtered_tweets

if __name__=='__main__':

    if len(argv)!=2:
        print "Trending tags file not provided, obtaining trending tags first."
        # Get trending hashtags
        trending_hashtags=get_trending_hashtags(ts.api)
        print "Trending hashtags obtained."
    elif len(argv)>2:
        print "Usage: %s <trending_tags_file>"%argv[0]
        quit()
    else:
        f=open(argv[1],'r')
        trending_hashtags=pickle.load(f)
        f.close()
        print "Trending hashtags obtained from file %s."%argv[1]
#    # Get filtered tweets
    filtered_tweets=get_filtered_tweets(ts.auth, trending_hashtags, 50000)
    print "Filtered tweets obtained."
