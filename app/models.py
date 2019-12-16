from django.conf import settings
from django.db import models

from django.utils import timezone


class Account(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dateCreated = models.DateTimeField(default=timezone.now)
    balance = models.IntegerField(default=0)

    def getLastTransaction(self):
        return Transaction.objects.filter(account_id=self.id).order_by('dateCreated').last()


class Transaction(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(choices=[('outcome', 'income')], max_length=20)
    amount = models.IntegerField()
    dateCreated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} {} {} {}".format(self.account.name, self.name, self.type, self.dateCreated)


class Debt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    amount = models.IntegerField(default=0)
    note = models.TextField()
    dateCreated = models.DateTimeField(default=timezone.now)
