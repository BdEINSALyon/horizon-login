from django.forms import Form
from django import forms


class AuthenticationForm(Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
