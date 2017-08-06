from django.contrib.auth.models import User, Group
from rest_framework import serializers

from login import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'is_superuser', 'is_active', 'permissions')
        read_only_fields = ('is_superuser', 'is_active', 'email', 'permissions')
        depth = 1


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Permission
        fields = ('name', 'description')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = ('name', 'description')
