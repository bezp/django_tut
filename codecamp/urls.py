from django.conf.urls import url

from . import views


app_name = 'cc'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.view, name='index'),
    url(r'^ajax/$', views.ajax, name='ajax'),
    url(r'^weather/$', views.weather, name='weather'),
    url(r'^wiki/$', views.wiki, name='wiki'),
    url(r'^twitch/$', views.twitch, name='twitch'),
    url(r'^ideas/$', views.ideas, name='ideas'),
    url(r'^ideas2/$', views.ideas2, name='ideas2'),


]

