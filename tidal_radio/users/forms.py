# -*- coding: utf-8 -*-
""" Users' Forms """

from django import forms

""" Form used in login """
class LoginForm(forms.Form):
    # Tidal's username
    username = forms.CharField(label="Tidal's username")
    # Tidal's password
    password = forms.CharField(label="Tidal's password",
        widget=forms.PasswordInput())

