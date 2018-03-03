#!/usr/bin/python

import os
import pickle

dirs=os.listdir('.')
for name in dirs:
    if name.startswith('followers'):
        print "Reading %s"%name
        with open(name,'r') as f:
            followers=pickle.load(f)
            follower_array=[]
            for follower in followers:
                follower_array.append(follower.id)
            newfile=name[:-4]+'_array.txt'
            f=open(newfile,'w')
            pickle.dump(follower_array,f)
            f.close()
            print "File %s written"%newfile
print "Program complete"
