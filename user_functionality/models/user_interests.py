
from django.db import models
from accounts.models.regular_user import RegularUser
from user_functionality.models.interest import Interest


class UserInterests(models.Model):
    user = models.ForeignKey(RegularUser, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)
