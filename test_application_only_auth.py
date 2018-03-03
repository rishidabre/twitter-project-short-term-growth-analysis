#!/usr/bin/python

import json
from application_only_auth import Client

# The consumer secret is an example and will not work for real requests
# To register an app visit https://dev.twitter.com/apps/new
CONSUMER_KEY = # generated from twitter account
CONSUMER_SECRET = # generated from twitter account

client = Client(CONSUMER_KEY, CONSUMER_SECRET)

# Pretty print of tweet payload
tweet = client.request('https://api.twitter.com/1.1/statuses/show.json?id=316683059296624640')
print json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ':'))

# Show rate limit status for this application
status = client.rate_limit_status()
print status['resources']['search']
