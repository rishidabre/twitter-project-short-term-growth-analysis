#!/usr/bin/python

import tweepy_setup as ts
import os
import get_twitter_users
import glob
import pickle
import time

# Gets the last 100 users for each set of 100 users
def get_last_100():
    t1=time.time()*1000
    total_users=len(glob.glob('followers_*'))
    k=0
    for afile in os.listdir('.'):
        if afile.startswith('followers_'):
            k+=1
            file_path=os.path.relpath(afile)
            dir_path=file_path.split('_')[1][0:-4]
            # Create directories for followers of each of the 10 users if required
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            print "Going to get followers for followers of user: "+dir_path
            try:
                f=open(afile,'r')
                # Load followers from file
                followers=pickle.load(f)
                i=0
                total=len(followers)
                for follower in followers:
                    i+=1
                    fid=follower.id_str
                    fname=dir_path+'/next_followers_'+fid+'.txt'
                    print "Going to get followers for follower ID: "+fid
                    if not os.path.exists(fname):
                        # Get followers for each of the 100 followers
                        get_twitter_users.get_followers(ts.api, follower, 100)
                        # Dump followers to file
                        f=open(fname, 'w')
                        pickle.dump(followers, f)
                        f.close()
                    print "[%s of %s] Followers for followers of user '%s' obtained."%(i,total,fid)
            except Exception as e:
                print "Error loading followers for user %s: "%dir_path,
                print e
            finally:
                f.close()
            print "[%s of %s] All followers for user %s obtained."%(k,total_users,dir_path)
        print "All followers obtained."
    t2=time.time()*1000
    print "Total time taken for finding followers: %s second(s)"%(t2-t1)
    return

get_last_100()
