# -*- coding: utf-8 -*-
""" Users views """

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

import tidalapi

from . import forms

"""
    Tidal Users Login
"""
class LoginView(View):

    """
        Get request of Login
    """
    def get(self, request):
        html = 'users/login.html'
        form = forms.LoginForm()
        context = {
            'form': form
        }
        return render(request, html, context)

    """
        Post request of Login
    """
    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # Creating a session in tidal api
        session = tidalapi.Session()
        # Login
        session.login(username, password)
        return HttpResponse(str(session.user.id))

