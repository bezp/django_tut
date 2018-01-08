from django.shortcuts import render
from .models import Art
from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms
import urllib3
from xml.dom import minidom
from collections import namedtuple
# Create your views here.


# funct to get coords of ppl submitting... hav an example ip  -- results in lat and lon
IP_URL = 'http://api.hostip.info/?ip='
def get_coords(ip):
    #ip = '4.2.2.2'  (denver) #hardcoded in... take out so there can be other inputs
    url = IP_URL + ip
    content = None  #start with nothing
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        content = r.data
    except urllib3.exceptions.HTTPError:
        return
    if content:
        d = minidom.parseString(content)
        coords = d.getElementsByTagName("gml:coordinates")
        if coords and coords[0].childNodes[0].nodeValue:
            lon, lat = coords[0].childNodes[0].nodeValue.split(',')
            return lat, lon


coord_points = []
def ascii(request):
    xtry = Art.objects.all()
    form = forms.AsciiForm()
    # aaa = request.META.get('REMOTE_ADDR') #testing local machine ip
    # aab = repr(get_coords(request.META.get('REMOTE_ADDR'))) #testing ip of user but we hardcoded one
    xtry = list(xtry) #so we dont loop over db more than once.. we just make a list we can go over when we ref xtry

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
    #xcoord_points = filter(None, (x.coords for x in xtry))  #can replace top func???

    GMAPS_URL = 'https://maps.googleapis.com/maps/api/staticmap?size=400x400&sensor=false&'
    #make the url link that will be used to make static pg w/ locations
    da_link = None  # start as None... if we hav coords, then we make 'da_link'
    if coord_points:
        markers = '&'.join('markers=%s,%s' % (p.lat, p.lon) for p in coord_points[-10:]) # hav a url link w/ last 10 submitters
        da_link = GMAPS_URL + markers

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
    #send stuff to html page
    return render(request, 'udacity/ascii.html', {'form': form, 'xtry': xtry,# 'aaa': aaa, 'aab': aab,
                                                 'a': da_link#, 'coord_points': coord_points,
                                                 })


