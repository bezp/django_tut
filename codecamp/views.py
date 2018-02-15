from django.shortcuts import render

# Create your views here.
def view(request):
    x = 'asdasd'
    return render(request, 'codecamp/jquery.html', {'x':x})



def ajax(request):
    return render(request, 'codecamp/ajax.html')


def weather(request):
    return render(request, 'codecamp/weather.html')

def wiki(request):
    return render(request, 'codecamp/wiki.html')

def twitch(request):
    return render(request, 'codecamp/twitch.html')

def ideas(request):
    return render(request, 'codecamp/ideas.html')

def ideas2(request):
    return render(request, 'codecamp/ideas2.html')

# def twitch(request):
#     return render(request, 'codecamp/twitch.html')