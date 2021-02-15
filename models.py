from django.db import models
import datetime
# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    date=models.DateField(default=datetime.datetime.today)
    score=models.IntegerField(default=0)
    def __str__(self):
        return self.username
