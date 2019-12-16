from django import forms

from app.models import *


class NewAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name', 'balance')


class EditAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name',)


class NewTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('name', 'amount')


class NewDebtForm(forms.ModelForm):
    class Meta:
        model = Debt
        exclude = ('user', 'dateCreated')
