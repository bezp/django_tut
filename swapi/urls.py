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
    url(r'^url/$', views.xurl, name='xurl'),
]

# # ex: /polls/5/
# url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
# # ex: /polls/5/results/
# url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
# # ex: /polls/5/vote/
# url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),