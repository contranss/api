__author__ = 'theofilis'

from django.db import models

from django.contrib.auth.models import User


class Driver(models.Model):
    user = models.OneToOneField(User)