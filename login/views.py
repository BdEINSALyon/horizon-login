from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from login.forms import AuthenticationForm


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def form_valid(self, form):
        user = authenticate(self.request, username=form.data['login'], password=form.data['password'])
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.request.POST.get('next', '/'))
        else:
            return super().form_invalid(form)


