from django.db import models

# Create your models here.
class Subject(models.Model):
    subject = models.CharField(max_length=100)
    choice_1 = models.CharField(max_length=100)
    choice_2 = models.CharField(max_length=100)


class Vote(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    choice = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
