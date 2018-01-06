from django.conf.urls import url

from . import views


app_name = 'udacity'
urlpatterns = [

    url(r'^$', views.ascii, name='ascii'),

]