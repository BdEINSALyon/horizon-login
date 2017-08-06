from django.contrib import admin


# Register your models here.
from login.models import Permission, Team


class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Permission, PermissionAdmin)


class TeamsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Team, TeamsAdmin)
