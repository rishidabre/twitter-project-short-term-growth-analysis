#!/usr/bin/python

from sys import argv
from os import listdir, rename

if len(argv)!=4:
    print "Usage: %s <from_dir> <to_dir> <number>"%argv[0]
    quit()
dirs=listdir(argv[1])
i=0
for dir in dirs:
    i+=1
    split=dir.split('/')
    fname=split[len(split)-1]
    print "Moving %s"%fname
    rename(argv[1]+'/'+dir,argv[2]+'/'+fname)
    print "Moved %s"%fname
    if i>=int(argv[3]):
        break
print "Complete"
