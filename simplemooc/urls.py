from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from core.views import home

urlpatterns = [
    url(r'^', include('core.urls')),
    path('admin/', admin.site.urls),
]
