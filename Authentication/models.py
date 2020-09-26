from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    degree = models.CharField(max_length=150, null=True, blank=True)
    facebook_ac = models.CharField(max_length=100, null=True, blank=True)
   


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "UserData"
        verbose_name_plural = "UserDataBase"