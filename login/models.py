from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Permission(models.Model):
    name = models.CharField(unique=True, verbose_name='Nom', max_length=255)
    description = models.CharField(verbose_name='Description', max_length=511)
    inherits = models.ForeignKey('Permission', on_delete=models.CASCADE, blank=True, null=True, related_name='sub_permissions')
    team = models.ForeignKey('Team', on_delete=models.CASCADE, blank=True, null=True, related_name='permissions', verbose_name='Equipe lié')
    users = models.ManyToManyField(User, related_name='permissions', verbose_name='Membres')

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(unique=True, verbose_name='Nom', max_length=255)
    description = models.CharField(verbose_name='Description', max_length=511)
