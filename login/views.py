from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect

from django.views.generic import FormView
from oauth2_provider.contrib.rest_framework import IsAuthenticatedOrTokenHasScope
from rest_framework import viewsets

from login import models, serializers
from login.forms import AuthenticationForm
from login.serializers import UserSerializer, GroupSerializer


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def form_valid(self, form):
        user = authenticate(self.request, username=form.data['login'], password=form.data['password'])
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.request.GET.get('next', '/'))
        else:
            return super().form_invalid(form)


class PermissionsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    required_scopes = ['permissions']
    queryset = models.Permission.objects.all()
    serializer_class = serializers.PermissionSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    required_scopes = ['users']
    queryset = User.objects.all()
    serializer_class = UserSerializer
