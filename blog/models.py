from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class crudst(models.Model):
    stname=models.CharField(max_length=200)
    stemail=models.CharField(max_length=100)
    staddress=models.CharField(max_length=150)
    stmobile=models.IntegerField()
    stgender=models.CharField(max_length=1)

class crudst1(models.Model):
    stname=models.CharField(max_length=200)
    stemail=models.CharField(max_length=100)
    staddress=models.CharField(max_length=150)
    stmobile=models.IntegerField()
    stgender=models.CharField(max_length=1)