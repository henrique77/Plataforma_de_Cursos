from django.conf.urls import url
from django.contrib import admin
from django.urls import path

import core
from core.views import home, contact
from courses.views import index, details, enrollment

urlpatterns = [
    #Colocar nome na url facilita a buscas posteriores
    url(r'^$', index, name='index'),
    #url(r'^(?P<pk>\d+)/$', details, name='details'),
    url(r'^(?P<slug>[\w_-]+)/$', details, name='details'),
    url(r'^(?P<slug>[\w_-]+)/inscricao$', enrollment, name='enrollment'),
]