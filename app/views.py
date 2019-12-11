from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from app.forms import NewAccountForm
from app.models import Account


def homepage(request):
    return render(request, 'homepage.html')


@login_required(login_url='/accounts/login/')
def accountsList(request):
    accounts = Account.objects.filter(user_id=request.user.id)
    return render(request, 'accounts/accounts.html', {'accounts': accounts})


@login_required(login_url='/accounts/login/')
def newAccount(request):
    if request.method == 'POST':
        form = NewAccountForm(request.POST)
        if form.is_valid:
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, 'Form submission successful')
            return redirect('accounts')
        else:
            messages.error(request, 'Form submission failed')
    else:
        form = NewAccountForm()
    return render(request, 'accounts/newAccount.html', {'form': form})
