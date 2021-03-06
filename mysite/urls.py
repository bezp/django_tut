"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from . import views #this is for courses app
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^quote/', include('udacity.urls')),
    url(r'^cc/', include('codecamp.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^swapi/', include('swapi.urls')),
    #url(r'^course_admin/', include(admin.site.urls)), #added course_ to url route # removed cause only 1 admind and u just need to register the app
    url(r'^s$', views.hello_world),
    url(r'^prev$', views.shello_world),
    url(r'^$', views.port_prev, name='profilecontact'),
]

urlpatterns += staticfiles_urlpatterns()

