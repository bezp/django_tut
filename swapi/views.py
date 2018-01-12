from django.shortcuts import render

# Create your views here.




















import urllib3
from xml.dom import minidom

import certifi

import json
from pprint import pprint



def get_coords():
    url = 'https://swapi.co/api/'
    content = None  #start with nothing
    try:
        http = urllib3.PoolManager(
                                        cert_reqs='CERT_REQUIRED',
                                        ca_certs=certifi.where())
        r = http.request('GET', url)
        content = r.data
    except urllib3.exceptions.HTTPError:
        return
    if content:
        x = json.loads(content)
        print (len(x))
        print (x)
        # print (len(x))
        # print (x['title']) #a new hope
        # print (x['episode_id']) #4
        # print (x['director']) #george lucas
        # return x #dictionary of everything




print (get_coords())










# response = urllib.request.urlopen('http://api.hostip.info/?ip=4.2.2.2')
# html = response.read()
# print (html)



# http = urllib3.PoolManager(
#     cert_reqs='CERT_REQUIRED',
#     ca_certs=certifi.where())
#
# r = http.request('GET', 'http://api.hostip.info/?ip=4.2.2.2')
# content = r.data
# print(content)









