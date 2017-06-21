# -*- coding: utf-8 -*-
""" Users urls """

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.LoginView.as_view(), name='users_login'),
    url(r'^profile/', views.ProfileView.as_view(), name='users_profile')
]

