#not added to git... im just testing a naked main url for pythonanywhere

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")