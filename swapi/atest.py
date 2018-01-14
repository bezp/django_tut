
from django.shortcuts import render

# Create your views here.

import urllib3
import certifi
import json


def get_films():
    url = 'https://swapi.co/api/films/'
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
        z = x
        return z['count']

print (get_films())