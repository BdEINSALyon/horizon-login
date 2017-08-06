from django.conf.urls import url, include
from rest_framework import routers

from login.views import UserViewSet, LoginView, PermissionsViewSet

# REST Framework Router for API
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'permissions', PermissionsViewSet)

# Main URLS
urlpatterns = [
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Mount API on v1/ because we can need later to use v2/ for new API
    url(r'^api/v1/', include(router.urls)),

    # Main login page for public users
    url(r'^accounts/login/$', LoginView.as_view()),

]
