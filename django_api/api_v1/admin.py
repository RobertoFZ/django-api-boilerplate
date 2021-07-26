from django.contrib import admin
from django_api.api_v1.models import (
    User,
    Profile,
)

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
