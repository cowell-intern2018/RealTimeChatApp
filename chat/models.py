from django.db import models

# Create your models here.

class User(models.Model):
    id_user = models.IntegerField()
    user_name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)

    def __str__(self):
        return self.id_user
