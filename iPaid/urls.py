"""iPaid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import app.views

urlpatterns = [
    path('', app.views.homepage, name='homepage'),
    path('account/', include('django.contrib.auth.urls')),
    path('accounts/', app.views.accountsGetList, name='accountsGetList'),
    path('accounts/<int:account_id>/', app.views.accountsGetDetail, name='accountsGetDetail'),
    path('accounts/new/', app.views.newAccount, name='newAccount'),
    path('accounts/edit/<int:account_id>/', app.views.editAccount, name='editAccount'),
    path('accounts/delete/<int:account_id>/', app.views.deleteAccount, name='deleteAccount'),
    path('accounts/new/<transaction_type>/<int:account_id>/', app.views.newTransaction, name='newTransaction'),
    path('accounts/transaction/delete/<int:transaction_id>/', app.views.deleteTransaction, name='deleteTransaction'),
    path('debts/', app.views.debtsGetList, name='debtsGetList'),
    path('debts/new/', app.views.newDebt, name='newDebt'),
    path('debts/edit/<debt_id>', app.views.editDebt, name='editDebt'),
    path('debts/delete/<debt_id>', app.views.deleteDebt, name='deleteDebt'),
    path('admin/', admin.site.urls),
]
