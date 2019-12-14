from django.conf import settings
from django.db import models
from datetime import datetime


class Account(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dateCreated = models.DateTimeField(default=datetime.now)
    balance = models.IntegerField(default=0)


class Transaction(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(choices=[('outcome', 'income')], max_length=20)
    amount = models.IntegerField()
    dateCreated = models.DateTimeField(default=datetime.now)
