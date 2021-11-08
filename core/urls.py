from django.conf.urls import url
from django.contrib import admin
from django.urls import path

import core
from core.views import home, contact

urlpatterns = [
    #Colocar nome na url facilita a buscas posteriores
    url(r'^$', home, name='home'),
    url(r'^contato/$', contact, name='contact'),
]