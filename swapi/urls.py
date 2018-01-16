from django.conf.urls import url

from . import views

app_name = 'swapi'
urlpatterns = [
    # url(r'^$', views., name=''),
    url(r'^$', views.main, name='main'),
    url(r'^films/$', views.films, name='films'),
    url(r'^people/$', views.people, name='people'),
    url(r'^species/$', views.species, name='species'),
    url(r'^planets/$', views.planets, name='planets'),
    url(r'^vehicles/$', views.vehicles, name='vehicles'),
    url(r'^starships/$', views.starships, name='starships'),

]

