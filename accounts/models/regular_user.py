from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User


class RegularUser(AbstractBaseUser):
    # user contains first name, last name, email, and password
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    university = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=30, blank=True)
    short_bio = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    age = models.IntegerField()
    preference = models.CharField(max_length=20, blank=True)

    def get_university(self):
        return self.university.__str__()

    def get_short_bio(self):
        return self.short_bio.__str__()
