from django.db import models


# Create your models here.
class Member(models.Model):
    location_name = models.CharField(max_length=50)
    town_name = models.CharField(max_length=50)


