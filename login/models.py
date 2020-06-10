from django.db import models
# from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    username = models.CharField(max_length=50, default="")
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    email = models.EmailField(primary_key=True, default="")
    password = models.CharField(max_length=50, default="")
    # image = models.ImageField('choose your photo',upload_to='profile_pic')

    def __str__(self):
        return self.username
