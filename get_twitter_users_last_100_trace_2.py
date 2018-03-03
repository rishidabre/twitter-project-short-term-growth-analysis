#!/usr/bin/python

import tweepy_setup as ts
import os
import get_twitter_users
import glob
import pickle
import time

# Gets the last 100 users for each set of 100 users
def get_last_100():
    t1=time.time()
    total_users=len(glob.glob('*trace_2*'))
    k=0
    for afile in os.listdir('.'):
        if afile.endswith('trace_2.txt'):
            k+=1
            file_path=os.path.relpath(afile)
            dir_path=file_path.split('_')[1]+'_2'
            # Create directories for followers of each of the 10 users if required
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            print "Going to get followers for followers of user: "+dir_path[:-2]
            try:
                f=open(afile,'r')
                # Load followers from file
                followers=pickle.load(f)
                i=0
                total=len(followers)
                failed_ids=[]
                for follower in followers:
                    i+=1
                    fid=follower.id_str
                    fname=dir_path+'/next_followers_'+fid+'.txt'
                    print "Going to get followers for follower ID: "+fid
                    if not os.path.exists(fname):
                        try:
                            # Get followers for each of the 100 followers
                            get_twitter_users.get_followers(ts.api, follower, 100)
                        except Exception as e:
                            print "Error getting followers for %s"%fid
                            print e
                            failed_ids.append(fid)
                            continue
                        # Dump followers to file
                        f=open(fname, 'w')
                        pickle.dump(followers, f)
                        f.close()
                    print "[%s of %s] Followers for followers of user '%s' obtained."%(i,total,fid)
                if len(failed_ids)>0:
                    f_failed=open("failed_ids_for_%s.txt"%dir_path[:-2],'w')
                    pickle.dump(failed_ids,f_failed)
                    f_failed.close()
            except Exception as e:
                print "Error loading followers for user %s: "%dir_path,
                print e
            finally:
                f.close()
            print "[%s of %s] All followers for user %s obtained."%(k,total_users,dir_path)
        print "All followers obtained."
    t2=time.time()
    print "Total time taken for finding followers: %s second(s)"%(t2-t1)
    return

get_last_100()
