from django.urls import path
from django.conf.urls import url, include
from django_api.api_v1.urls import users
from django_api.api_v1.urls import auth

urlpatterns = [
    # Base URL's
    path("users/", include((users, "users"))),
    path("auth/", include((auth, "auth"))),
]
