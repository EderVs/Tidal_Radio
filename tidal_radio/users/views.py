# -*- coding: utf-8 -*-
""" Users' views """

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

import tidalapi

from . import forms
from . import utils

class LoginView(View):
    """
        Tidal Users Login
    """

    def get(self, request):
        """
            Get request of Login
        """
        html = 'users/login.html'
        form = forms.LoginForm()
        context = {
            'form': form
        }
        return render(request, html, context)

    def post(self, request):
        """
            Post request of Login
        """
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # Creating a session in tidal api
        session = tidalapi.Session()
        # Tidal Login
        session.login(username, password)
        # Django Login just to get the username in session
        user = authenticate(username=username, password=password)
        if user is None:
            # Create new user
            user = User.objects.create_user(username, '', password)
        
        utils.add_tidal_session(username, session)
        return HttpResponse(str(session.user.id))

