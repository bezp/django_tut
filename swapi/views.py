from django.shortcuts import render, HttpResponseRedirect, HttpResponse
import urllib3
import certifi
import json
from django.core.urlresolvers import reverse


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
    # edit = edit.replace('%2D', "-")
    return edit

def search(request, tuple_list, num):
    r = request.META.get('QUERY_STRING')
    s = url_convert(r[num:])
    result = []
    for tup in tuple_list:
        if s.lower() in tup[0].lower() and s != '':
            result.append(tup[0])
    return result

error = 'Please enter a VALID query'
def xurl(request):
    result = search(request, li_people, 7)
    return render(request, 'swapi/xurl.html', {'r':result, 'error':error})




# def xurl(request):
#     r = request.META.get('QUERY_STRING') #get the value of what they submit...'people=luke'
#     s = url_convert(r[7:].lower())
#     if s:
#         s = s[0].capitalize() + s[1:]
#     result = []
#     for tup in li_species:
#         if s in tup[0] and s != '':
#             result.append(tup[0])
#     error = 'Please enter a VALID query'
#     return render(request, 'swapi/xurl.html', {'r':result, 'error':error})


def main(request):
    x = get_url_specific(6)
    return render(request, 'swapi/main.html', {'main': x})


def films(request):
    x = get_url_specific(0)
    x = x['results']
    ordered_list = sorted(x, key=lambda k: k['episode_id'])
    return render(request, 'swapi/films.html', {'films': ordered_list}) #films sent is a list of dict


li_people = [('Luke Skywalker', 1), ('C-3PO', 2), ('R2-D2', 3), ('Darth Vader', 4), ('Leia Organa', 5),
             ('Owen Lars', 6), ('Beru Whitesun lars', 7), ('R5-D4', 8), ('Biggs Darklighter', 9),
             ('Obi-Wan Kenobi', 10), ('Anakin Skywalker', 11), ('Wilhuff Tarkin', 12), ('Chewbacca', 13),
             ('Han Solo', 14), ('Greedo', 15), ('Jabba Desilijic Tiure', 16), ('Wedge Antilles', 18),
             ('Jek Tono Porkins', 19), ('Yoda', 20), ('Palpatine', 21), ('Boba Fett', 22), ('IG-88', 23),
             ('Bossk', 24), ('Lando Calrissian', 25), ('Lobot', 26), ('Ackbar', 27), ('Mon Mothma', 28),
             ('Arvel Crynyd', 29), ('Wicket Systri Warrick', 30), ('Nien Nunb', 31), ('Qui-Gon Jinn', 32),
             ('Nute Gunray', 33), ('Finis Valorum', 34), ('Padmé Amidala', 35), ('Jar Jar Binks', 36),
             ('Roos Tarpals', 37), ('Rugor Nass', 38), ('Ric Olié', 39), ('Watto', 40), ('Sebulba', 41),
             ('Quarsh Panaka', 42), ('Shmi Skywalker', 43), ('Darth Maul', 44), ('Bib Fortuna', 45),
             ('Ayla Secura', 46), ('Ratts Tyerell', 47), ('Dud Bolt', 48), ('Gasgano', 49), ('Ben Quadinaros', 50),
             ('Mace Windu', 51), ('Ki-Adi-Mundi', 52), ('Kit Fisto', 53), ('Eeth Koth', 54), ('Adi Gallia', 55),
             ('Saesee Tiin', 56), ('Yarael Poof', 57), ('Plo Koon', 58), ('Mas Amedda', 59), ('Gregar Typho', 60),
             ('Cordé', 61), ('Cliegg Lars', 62), ('Poggle the Lesser', 63), ('Luminara Unduli', 64),
             ('Barriss Offee', 65), ('Dormé', 66), ('Dooku', 67), ('Bail Prestor Organa', 68), ('Jango Fett', 69),
             ('Zam Wesell', 70), ('Dexter Jettster', 71), ('Lama Su', 72), ('Taun We', 73), ('Jocasta Nu', 74),
             ('R4-P17', 75), ('Wat Tambor', 76), ('San Hill', 77), ('Shaak Ti', 78), ('Grievous', 79), ('Tarfful', 80),
             ('Raymus Antilles', 81), ('Sly Moore', 82), ('Tion Medon', 83), ('Finn', 84), ('Rey', 85),
             ('Poe Dameron', 86), ('BB8', 87)]
def people(request):
    r = request.META.get('QUERY_STRING')
    s = url_convert(r[7:].lower())
    if s:
        s = s[0].capitalize() + s[1:]
    error = 'Please enter a VALID query'
    first_item = None
    other_choices = []
    result = []  # list of numbers
    for tup in li_people:
        if s in tup[0] and s != '':  # need s!='' b/c w/o it givs eveything
            result.append(tup[1])
    content = []
    for num in result:
        detail_url = get_url_specific(1, num)
        content.append(detail_url)
    if content:
        first_item = [content[0]]  # list of dict
        other_choices = [c['name'] for c in content]
    return render(request, 'swapi/people.html', {'people': first_item, 'others': other_choices, 'error': error})


li_planets = [('Tatooine', 1), ('Alderaan', 2), ('Yavin IV', 3), ('Hoth', 4), ('Dagobah', 5), ('Bespin', 6),
              ('Endor', 7), ('Naboo', 8), ('Coruscant', 9), ('Kamino', 10), ('Geonosis', 11), ('Utapau', 12),
              ('Mustafar', 13), ('Kashyyyk', 14), ('Polis Massa', 15), ('Mygeeto', 16), ('Felucia', 17),
              ('Cato Neimoidia', 18), ('Saleucami', 19), ('Stewjon', 20), ('Eriadu', 21), ('Corellia', 22),
              ('Rodia', 23), ('Nal Hutta', 24), ('Dantooine', 25), ('Bestine IV', 26), ('Ord Mantell', 27),
              ('unknown', 28), ('Trandosha', 29), ('Socorro', 30), ('Mon Cala', 31), ('Chandrila', 32),
              ('Sullust', 33), ('Toydaria', 34), ('Malastare', 35), ('Dathomir', 36), ('Ryloth', 37),
              ('Aleen Minor', 38), ('Vulpter', 39), ('Troiken', 40), ('Tund', 41), ('Haruun Kal', 42),
              ('Cerea', 43), ('Glee Anselm', 44), ('Iridonia', 45), ('Tholoth', 46), ('Iktotch', 47),
              ('Quermia', 48), ('Dorin', 49), ('Champala', 50), ('Mirial', 51), ('Serenno', 52),
              ('Concord Dawn', 53), ('Zolan', 54), ('Ojom', 55), ('Skako', 56), ('Muunilinst', 57), ('Shili', 58),
              ('Kalee', 59), ('Umbara', 60), ('Jakku', 61)]
def planets(request):

    # x = get_url(2)
    # x = x['results']
    return render(request, 'swapi/planets.html', {'planets': li_dict})



li_species = [('Human', 1), ('Droid', 2), ('Wookiee', 3), ('Rodian', 4), ('Hutt', 5), ("Yoda's species", 6),
             ('Trandoshan', 7), ('Mon Calamari', 8), ('Ewok', 9), ('Sullustan', 10), ('Neimodian', 11),
             ('Gungan', 12), ('Toydarian', 13), ('Dug', 14), ("Twi'lek", 15), ('Aleena', 16), ('Vulptereen', 17),
             ('Xexto', 18), ('Toong', 19), ('Cerean', 20), ('Nautolan', 21), ('Zabrak', 22), ('Tholothian', 23),
             ('Iktotchi', 24), ('Quermian', 25), ('Kel Dor', 26), ('Chagrian', 27), ('Geonosian', 28),
             ('Mirialan', 29), ('Clawdite', 30), ('Besalisk', 31), ('Kaminoan', 32), ('Skakoan', 33), ('Muun', 34),
             ('Togruta', 35), ('Kaleesh', 36), ("Pau'an", 37)]
def species(request):
    r = request.META.get('QUERY_STRING')
    s = url_convert(r[8:].lower())
    if s:
        s = s[0].capitalize() + s[1:]
    error = 'Please enter a VALID query'
    first_item = None
    other_choices = []
    result = [] #list of numbers
    for tup in li_species:
        if s in tup[0] and s != '':  #need s!='' b/c w/o it givs eveything
            result.append(tup[1])
    content = []
    for num in result:
        detail_url = get_url_specific(3, num)
        content.append(detail_url)
    if content:
        first_item = [content[0]] #list of dict
        other_choices = [c['name'] for c in content]
    return render(request, 'swapi/species.html', {'others': other_choices, 'error': error, 'link': first_item})


li_starships = [('CR90 corvette', 2), ('Star Destroyer', 3), ('Sentinel-class landing craft', 5), ('Death Star', 9),
                ('Millennium Falcon', 10), ('Y-wing', 11), ('X-wing', 12), ('TIE Advanced x1', 13), ('Executor', 15),
                ('Rebel transport', 17), ('Slave 1', 21), ('Imperial shuttle', 22),
                ('EF76 Nebulon-B escort frigate', 23), ('Calamari Cruiser', 27), ('A-wing', 28), ('B-wing', 29),
                ('Republic Cruiser', 31), ('Droid control ship', 32), ('Naboo fighter', 39)]
def starships(request):
    li_dict = []
    amount = list(range(1,2))
    for num in amount:
        try:
            x = get_url_specific(4, num)
            li_dict.append((x['name'], num))
        except KeyError:
            continue
    # x = x['results']
    return render(request, 'swapi/starships.html', {'starships': li_dict})


li_vehicles = [('Sand Crawler', 4), ('T-16 skyhopper', 6), ('X-34 landspeeder', 7), ('TIE/LN starfighter', 8),
               ('Snowspeeder', 14), ('TIE bomber', 16), ('AT-AT', 18), ('AT-ST', 19),
               ('Storm IV Twin-Pod cloud car', 20), ('Sail barge', 24), ('Bantha-II cargo skiff', 25),
               ('TIE/IN interceptor', 26), ('Imperial Speeder Bike', 30), ('Vulture Droid', 33),
               ('Multi-Troop Transport', 34), ('Armored Assault Tank', 35), ('Single Trooper Aerial Platform', 36),
               ('C-9979 landing craft', 37), ('Tribubble bongo', 38)]
def vehicles(request):

    x = get_url_specific(5)
    x = x['results']
    return render(request, 'swapi/vehicles.html', {'vehicles': x})













