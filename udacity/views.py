
from .models import Art
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms
from xml.dom import minidom
from collections import namedtuple
import requests

# funct to get coords of ppl submitting... hav an example ip  -- results in lat and lon
IP_URL = 'http://api.hostip.info/?ip='

def get_coords(ip):
    # ip = '4.2.2.2' # (denver) #hardcoded in... take out so there can be other inputs
    # ip = '192.206.151.131'
    # ip = '217.209.91.160'
    url = IP_URL + ip
    r = requests.get(url)
    content = r.text
    if content:
        d = minidom.parseString(content)
        coords = d.getElementsByTagName("gml:coordinates")
        if coords and coords[0].childNodes[0].nodeValue:
            lon, lat = coords[0].childNodes[0].nodeValue.split(',')
            return lat, lon


coord_points = []
def ascii(request):
    xtry = Art.objects.filter(
        pk__gte=47
    )
    form = forms.AsciiForm()
    xtry = list(xtry[::-1])

    #find ones w/ coords
    Point = namedtuple('Point', ['lat', 'lon']) # want to store coords as a namedtuple...
    b = ',' #keeping just to hav a var that might be used later
    for x in xtry:
        if Art.coords and b in x.coords:  #filter out coords that are '0' or None or hav a local host ip
            x,y = x.coords.split(b)
            x = x[2:-1]  #cutting out extra stuff b/c of how i had to store it...ex. [Point(lat='33.9262', lon='-117.21')]
            y = y[2:-2]
            if Point(x, y) not in coord_points:

                coord_points.append(Point(x, y))
            pass

    GMAPS_URL = 'https://maps.googleapis.com/maps/api/staticmap?size=700x370&sensor=false&'
    key = '&key=AIzaSyCftccJ8RWo6Rth9U4v8_F6oK8F8awk6Us'
    da_link = None  # start as None... if we hav coords, then we make 'da_link'
    da_link2 = None
    if coord_points:
        markers = '&'.join('markers=%s,%s' % (p.lat, p.lon) for p in coord_points) # amount of markers in url link
        da_link = GMAPS_URL + markers + key

    if coord_points:
        markers = '&'.join('markers=%s,%s' % (p.lat, p.lon) for p in coord_points[-1:]) #make only the last marker url so last location...
        da_link2 = GMAPS_URL + markers + key



    if request.method == 'POST':
        form = forms.AsciiForm(request.POST)
        if form.is_valid():
            # lookup users coords from IP
            coords = get_coords(request.META.get('REMOTE_ADDR'))  #get ip using funct and saviing it further down
            #if we get it, add to art model
            if coords:
                x = form.save(commit=False)
                x.coords = coords
                x.save()  #saving the coords that we find from user using hostip
            # regular save on model and return back to same page w/ blank form
            form.save()
            return HttpResponseRedirect(reverse('udacity:ascii'))
    return render(request, 'udacity/udacity.html', {'form': form, 'xtry': xtry,# 'aaa': aaa, 'aab': aab,
                                                 'a': da_link#, 'coord_points': coord_points,
                                                  , 'b': da_link2
                                                 })






