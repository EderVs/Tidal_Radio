# -*- coding: utf-8 -*-
""" Users views """

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

"""
    Tidal Users Login
"""
class LoginView(View):

    """
        Get request of Login
    """
    def get(self, request):
        return HttpResponse('Login')

