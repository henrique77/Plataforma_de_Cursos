from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from core.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    path('admin/', admin.site.urls),
]
