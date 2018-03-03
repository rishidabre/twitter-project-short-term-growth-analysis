#!/usr/bin/python

import tweepy_setup as ts
import json

# Checks the rate limit status and quits the program
def check_rate_limit_status():
    rate_limit_status=ts.api.rate_limit_status()
    print "Rate limit status: "
    print json.dumps(rate_limit_status, sort_keys=True, indent=4, separators=(',', ':'))
    return

if __name__=='__main__':
    check_rate_limit_status()
