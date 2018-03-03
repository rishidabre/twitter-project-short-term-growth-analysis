#!/usr/bin/python

import tweepy_setup as ts
import json
import tweepy
import time
import pickle
import os

#print json.dumps(result, sort_keys=True, indent=4, separators=(',', ':'))

if __name__=='__main__':
    t1=time.time()
    dirs=os.listdir('.')
    for name in dirs:
        if name.endswith('array.txt'):
            print "Reading file %s"%name
            f=open(name,'r')
            follower_ids=pickle.load(f)
            f.close()
            newfile=name.replace('array','matrix')
            if os.path.exists(newfile):
                print "File %s already exists"%newfile
                continue
            follower_matrix={}
            i=0
            for id1 in follower_ids:
                i+=1
                ta1=time.time()
                followers_to_check=ts.api.followers_ids(id1)
                j=0
                for id2 in follower_ids:
                    j+=1
                    print "Working with %sx%s"%(i,j)
                    follows=(id2 in followers_to_check)
                    if not follower_matrix.get(id1):
                        follower_matrix[id1]={}
                    follower_matrix.get(id1)[id2]=follows
                ta2=time.time()
                print "Time taken for follower ID %s: %s seconds"%(id1,(ta2-ta1))
            with open(newfile,'w') as f:
                pickle.dump(follower_matrix,f)
            print "Written %s"%newfile
    t2=time.time()
    print "Program completed in %s seconds."%(t2-t1)
