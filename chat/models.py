from django.db import models
from django.contrib.auth.models import User


class UserCustomized(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.id
        