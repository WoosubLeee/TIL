from django.db import models
from django.conf import settings

# Create your models here.
class Reservation(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    personnel = models.IntegerField()


class Comment(models.Model):
    content = models.CharField(max_length=100)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
