import django.contrib.auth.views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login

from accounts.views import register, dashboard, edit, edit_password, password_reset, password_reset_confirm

import accounts.views
import core
from core.views import home, contact

urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    #path('sair/', LoginView.as_view(next_page='/'), name='logout'),
    path('sair/', logout_then_login, {'login_url': '/'}, name='logout'),
    url(r'^cadastre-se/$', register, name='register'),
    url(r'^nova-senha/$', password_reset, name='password_reset'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^editar/$', edit, name='edit'),
    url(r'^editar-senha/$', edit_password, name='edit_password'),
    #url(r'^entrar/$', LoginView.as_view(), name='login'),
    #url(r'^entrar/$', auth_login, {'template_name': 'account/login.html'}, name='login'),
]