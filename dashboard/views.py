from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from .models import Account, Product

# Create your views here.

@login_required
def home(request):
    context = {
        'title': 'Home',
        'accounts': Account.objects.filter(user = request.user),
    }

    return render(request, 'dashboard/home.html', context)


class AccountCreateView(CreateView):
    model = Account
    fields = [
        'name',
        'account_type',
        'bank_name',
        'balance'
    ]
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

class ProductCreateView(CreateView):
    model = Product
    success_url = '/'
    fields = [
        'name',
        'account',
        'product_type',
        'price',
    ]

    def form_valid(self, form):
        account_pk = form.cleaned_data.get('account').pk

        balance = Account.objects.filter(user = self.request.user, pk = account_pk).values('balance')[0]['balance']

        new_balance = int(balance) - int(form.cleaned_data.get('price'))

        form.instance.user = self.request.user
        Account.objects.filter(user = self.request.user, pk = account_pk).update(balance=new_balance)

        return super().form_valid(form)