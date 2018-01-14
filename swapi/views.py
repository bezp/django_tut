from django.shortcuts import render, HttpResponseRedirect, HttpResponse

# Create your views here.

import urllib3
import certifi
import json
from django.core.urlresolvers import reverse


li_species = [('Human', 1), ('Droid', 2), ('Wookiee', 3), ('Rodian', 4), ('Hutt', 5), ("Yoda's species", 6),
             ('Trandoshan', 7), ('Mon Calamari', 8), ('Ewok', 9), ('Sullustan', 10), ('Neimodian', 11),
             ('Gungan', 12), ('Toydarian', 13), ('Dug', 14), ("Twi'lek", 15), ('Aleena', 16), ('Vulptereen', 17),
             ('Xexto', 18), ('Toong', 19), ('Cerean', 20), ('Nautolan', 21), ('Zabrak', 22), ('Tholothian', 23),
             ('Iktotchi', 24), ('Quermian', 25), ('Kel Dor', 26), ('Chagrian', 27), ('Geonosian', 28),
             ('Mirialan', 29), ('Clawdite', 30), ('Besalisk', 31), ('Kaminoan', 32), ('Skakoan', 33), ('Muun', 34),
             ('Togruta', 35), ('Kaleesh', 36), ("Pau'an", 37)]

def get_url(value):
    urls = ['https://swapi.co/api/films/', 'https://swapi.co/api/people/',
            'https://swapi.co/api/planets/', 'https://swapi.co/api/species/',
            'https://swapi.co/api/starships/', 'https://swapi.co/api/vehicles/',
            'https://swapi.co/api/'
            ]
    url = urls[value]

    content = None
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
        return x

def get_url_specific(value, number=None):
    urls = ['https://swapi.co/api/films/', 'https://swapi.co/api/people/',
            'https://swapi.co/api/planets/', 'https://swapi.co/api/species/',
            'https://swapi.co/api/starships/', 'https://swapi.co/api/vehicles/',
            'https://swapi.co/api/'
            ]
    url = urls[value]
    if number:
        url += str(number)
    content = None
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
        return x

def url_convert(string): #convert '+' to a ' 'space, etc... for url values
    edit = string
    edit = edit.replace('+', ' ')
    edit = edit.replace('%27', "'")

    return edit

def xurl(request):
    r = request.META.get('QUERY_STRING') #get the value of what they submit...'people=luke'
    r = r[7:].lower()
    s = url_convert(r)
    result = []
    for tup in li_species:
        if s.title() in tup[0] and s != '':
            result.append(tup[1]) #returns the number part of tuple
    return render(request, 'swapi/xurl.html', {'r':result})


def main(request):
    x = get_url(6)
    return render(request, 'swapi/main.html', {'main': x})

def films(request):
    x = get_url(0)
    x = x['results']
    ordered_list = sorted(x, key=lambda k: k['episode_id'])
    return render(request, 'swapi/films.html', {'films': ordered_list}) #films sent is a list of dict


def people(request):
    li_dict = []
    amount = list(range(16,20))

    for num in amount:
        try:
            x = get_url_specific(1, num)
            li_dict.append(x['name'])
        except KeyError:
            continue
    # x = x['results']
    # name_list = sorted(x, key=lambda k: k['name'])
    return render(request, 'swapi/people.html', {'people': li_dict})

def planets(request):
    x = get_url(2)
    x = x['results']
    return render(request, 'swapi/planets.html', {'planets': x})




def species(request):
    r = request.META.get('QUERY_STRING')
    r = r[8:].lower()
    error = None
    first_item = None
    try:
        if not all(x.isalpha() or x == '\'' or x == ' ' for x in r):
            error = 'Please enter a VALID query using the english alphabet'
    except IndexError:
        pass
    s = url_convert(r)
    result = []
    for tup in li_species:
        if s.title() in tup[0] and s != '':  #need s!='' b/c w/o it givs eveything
            result.append(tup[1])
    content = []
    for num in result:
        detail_url = get_url_specific(3, num)
        content.append(detail_url)
    if content:
        first_item = [content[0]] #list of dict
    return render(request, 'swapi/species.html', {'species': result, 'error': error, 'link': first_item})

def starships(request):
    x = get_url(4)
    x = x['results']
    return render(request, 'swapi/starships.html', {'starships': x})

def vehicles(request):
    x = get_url(5)
    x = x['results']
    return render(request, 'swapi/vehicles.html', {'vehicles': x})







# def species(request):
#     li_dict = []
#     amount = list(range(1, 3))
#
#     for num in amount:
#         try:
#             x = get_url_specific(3, num)
#             li_dict.append((x['name'], num))
#         except KeyError:
#             continue
#     # x = get_url_specific(3)
#     # x = x['results']
#     return render(request, 'swapi/species.html', {'species': li_dict})




#
# def get_coords(valuex):
#     urls = ['https://swapi.co/api/films/', 'https://swapi.co/api/people/',
#             'https://swapi.co/api/planets/', 'https://swapi.co/api/species/',
#             'https://swapi.co/api/starships/', 'https://swapi.co/api/vehicles/'
#             ]
#     url = urls[valuex]
#
#     content = None
#     try:
#         http = urllib3.PoolManager(
#                                         cert_reqs='CERT_REQUIRED',
#                                         ca_certs=certifi.where())
#         r = http.request('GET', url)
#         content = r.data
#     except urllib3.exceptions.HTTPError:
#         return
#     if content:
#         x = json.loads(content)
#
#
#         # print (x)
#         # print (len(x))
#         # print (x['title']) #a new hope
#         # print (x['episode_id']) #4
#         # print (x['director']) #george lucas
#         # return x #dictionary of everything








# def get_films():
#     url = 'https://swapi.co/api/films/'
#     try:
#         http = urllib3.PoolManager(
#                                         cert_reqs='CERT_REQUIRED',
#                                         ca_certs=certifi.where())
#         r = http.request('GET', url)
#         content = r.data
#     except urllib3.exceptions.HTTPError:
#         return
#     if content:
#         x = json.loads(content)
#         return x











