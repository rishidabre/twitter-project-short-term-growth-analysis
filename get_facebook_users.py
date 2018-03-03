#!/usr/bin/python

import httplib

user_access_token=#generated from facebook account

try:
    mycon=httplib.HTTPSConnection('graph.facebook.com')
    headers={'access_token': user_access_token}
    params={}
    mycon.request('GET', '/v2.8/me', params, headers)
    response=mycon.getresponse()
    print response.read()
except Exception as e:
    print 'Error occurred'
    print e
finally:
    mycon.close()
