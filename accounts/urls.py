import django.contrib.auth.views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login

from accounts.views import register

import accounts.views
import core
from core.views import home, contact

urlpatterns = [
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    #path('sair/', LoginView.as_view(next_page='/'), name='logout'),
    path('sair/', logout_then_login, {'login_url': '/'}, name='logout'),

    url(r'^cadastre-se/$', register, name='register'),
    #url(r'^entrar/$', LoginView.as_view(), name='login'),
    #url(r'^entrar/$', auth_login, {'template_name': 'account/login.html'}, name='login'),
]