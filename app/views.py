from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from app.forms import *
from app.models import *


def homepage(request):
    return render(request, 'homepage.html')


@login_required(login_url='/accounts/login/')
def accountsGetList(request):
    accounts = Account.objects.filter(user_id=request.user.id)
    return render(request, 'accounts/getList.html', {'accounts': accounts})


@login_required(login_url='/accounts/login/')
def accountsGetDetail(request, account_id):
    account = get_object_or_404(Account, id=account_id, user_id=request.user.id)
    transactions = Transaction.objects.filter(account_id=account_id).order_by('-dateCreated')
    return render(request, 'accounts/getDetail.html', {'account': account, 'transactions': transactions})


@login_required(login_url='/accounts/login/')
def newAccount(request):
    if request.method == 'POST':
        form = NewAccountForm(request.POST)
        if form.is_valid:
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, 'Účet byl vytvořen.')
            return redirect('accountsGetList')
        else:
            messages.error(request, 'Účet nebyl vytvořen!')
    else:
        form = NewAccountForm()
    return render(request, 'accounts/new.html', {'form': form})


@login_required(login_url='/accounts/login/')
def editAccount(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=account)
        if form.is_valid:
            form.save()
            messages.success(request, 'Účet byl upraven.')
            return redirect('accountsGetList')
        else:
            messages.error(request, 'Účet nebyl upraven!')
    else:
        form = EditAccountForm(instance=account)
    return render(request, 'accounts/edit.html', {'form': form, 'account': account_id})


@login_required(login_url='/accounts/login/')
def deleteAccount(request, account_id):
    account = get_object_or_404(Account, id=account_id, user_id=request.user.id)
    account.delete()
    return redirect('accountsGetList')


@login_required(login_url='/accounts/login/')
def newTransaction(request, transaction_type, account_id):
    if transaction_type not in ['income', 'outcome']:
        raise Http404
    account = get_object_or_404(Account, id=account_id, user_id=request.user.id)
    if request.method == 'POST':
        form = NewTransactionForm(request.POST)
        if form.is_valid:
            obj = form.save(commit=False)
            obj.account = account
            obj.type = transaction_type
            obj.save()

            if transaction_type == 'income':
                account.balance += obj.amount
            else:
                account.balance -= obj.amount
            account.save()

            messages.success(request, 'Transakce byla vytvořena.')
            return redirect('accountsGetList')
        else:
            messages.error(request, 'Transakce nebyla vytvořena!')
    else:
        form = NewTransactionForm()
    return render(request, 'transactions/new.html',
                  {'form': form, 'account': account, 'type': transaction_type})


@login_required(login_url='/accounts/login/')
def deleteTransaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    account = get_object_or_404(Account, id=transaction.account_id, user_id=request.user.id)
    if transaction.type == 'income':
        account.balance -= transaction.amount
    else:
        account.balance += transaction.amount
    account.save()
    transaction.delete()
    return redirect('accountsGetDetail', account.id)


@login_required(login_url='/accounts/login/')
def debtsGetList(request):
    debts = Debt.objects.filter(user_id=request.user.id).order_by('-dateCreated')
    return render(request, 'debts/getList.html', {'debts': debts})


@login_required(login_url='/accounts/login/')
def newDebt(request):
    if request.method == 'POST':
        form = NewDebtForm(request.POST)
        if form.is_valid:
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, 'Dluh byl vytvořen.')
            return redirect('debtsGetList')
        else:
            messages.error(request, 'Dluh nebyl vytvořen!')
    else:
        form = NewDebtForm()
    return render(request, 'debts/new.html', {'form': form})


@login_required(login_url='/accounts/login/')
def editDebt(request, debt_id):
    debt = get_object_or_404(Debt, id=debt_id, user_id=request.user.id)
    if request.method == 'POST':
        form = NewDebtForm(request.POST, instance=debt)
        if form.is_valid:
            form.save()
            messages.success(request, 'Dluh byl upraven.')
            return redirect('debtsGetList')
        else:
            messages.error(request, 'Dluh nebyl upraven!')
    else:
        form = NewDebtForm(instance=debt)
    return render(request, 'debts/edit.html', {'form': form, 'debt': debt_id})


@login_required(login_url='/accounts/login/')
def deleteDebt(request, debt_id):
    debt = get_object_or_404(Debt, id=debt_id, user_id=request.user.id)
    debt.delete()
    return redirect('debtsGetList')
