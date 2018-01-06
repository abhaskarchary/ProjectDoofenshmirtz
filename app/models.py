from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender')
    receiver = models.ForeignKey(User, related_name='receiver')
    content = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.pk + self.receiver

