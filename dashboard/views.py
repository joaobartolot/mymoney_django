from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView

from .models import Account, Product

# Custom mixins:

class CleanFieldMixin(object):
    # Method to remove the 'R$', ',' and the '.' in the currency fields
    def money_flied (self, field):
        prefix_removed = field[3:]

        cleaned_flied = ''
        for letter in prefix_removed:
            if letter != '.' and letter != ',':
                cleaned_flied += letter

        return int(cleaned_flied)

# Create your views here.

@login_required
def home(request):
    context = {
        'title': 'Home',
        'accounts': Account.objects.filter(user = request.user),
        'products': Product.objects.filter(user = request.user)
    }

    return render(request, 'dashboard/home.html', context)


class AccountCreateView(CleanFieldMixin, CreateView):
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
        balance = form.cleaned_data.get('balance')

        form.instance.balance = self.money_field(form.cleaned_data.get('balance'))

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
        price = form.cleaned_data.get('price')

        new_balance = balance - price

        form.instance.user = self.request.user
        Account.objects.filter(user = self.request.user, pk = account_pk).update(balance=new_balance)

        return super().form_valid(form)

class AccountListView(ListView):
    model = Account
    context_object_name = 'accounts'
    paginate_by = 20