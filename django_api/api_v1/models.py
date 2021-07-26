import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    def get_profile(self):
        return Profile.objects.get(user=self)

    def __str__(self):
        return self.email

    USER_ROLES = (
        ('admin', 'Administrador'),
        ('driver', 'Conductor'),
    )

    username = None
    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(
        max_length=200, default='driver', choices=USER_ROLES)
    on_route = models.BooleanField(default=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Profile(BaseModel):
    # Relations
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Attributes
    locale = models.CharField(default="es", max_length=2)
    phone = models.CharField(max_length=255, blank=True, null=True)
    municipality = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "%s Profile's" % (self.user.email)
