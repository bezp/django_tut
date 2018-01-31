from django.conf.urls import url

from . import views


app_name = 'cc'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.view, name='index'),
    url(r'^ajax/$', views.ajax, name='ajax'),
]

