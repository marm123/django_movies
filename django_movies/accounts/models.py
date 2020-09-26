from django.contrib.auth.models import User
from django.db import models
from django.db.models import OneToOneField, Model, IntegerField, CASCADE


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    shoe_size = IntegerField()
