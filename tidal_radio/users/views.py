# -*- coding: utf-8 -*-
""" Users views """

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

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

