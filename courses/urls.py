from django.conf.urls import url
from django.contrib import admin
from django.urls import path

import core
from core.views import home, contact
from courses.views import index

urlpatterns = [
    #Colocar nome na url facilita a buscas posteriores
    url(r'^$', index, name='index'),
]