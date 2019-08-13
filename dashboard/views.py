from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView

from .models import Account, Product

# Custom mixins:

class CustomMixin(object):
    # Method to remove the 'R$', ',' and the '.' in the currency fields
    def money_field(self, field, form):
        value = form.cleaned_data.get(field)

        if len(value.split(' ')) == 1:
            cleaned_field = '000'

        else:
            value = value.split(' ')[1]
            value = ''.join(value.split('.'))

            split_value = value.split(',')

            if len(split_value) == 1:
                cleaned_field = ''.join([split_value[0], '00'])
            else:
                if len(split_value[1]) == 1:
                    cleaned_field = ''.join([split_value[0], split_value[1] + '0'])
                else:
                    cleaned_field = ''.join(split_value)

        return cleaned_field

    def field_sum(self, query, field):
        values = query.values(field)
        if len(values) != 0:
            total = 0
            for value in values:
                total += value[field]

            total = str(total)

            return f'R$ {total[-2:]},{total[-2]}'
        else:
            return f'R$ 0,00'


# Create your views here.

@login_required
def home(request):
    context = {
        'title': 'Home',
        'accounts': Account.objects.filter(user = request.user),
        'products': Product.objects.filter(user = request.user)
    }

    return render(request, 'dashboard/home.html', context)


class AccountCreateView(CustomMixin, CreateView):
    model = Account
    success_url = '/'
    fields = [ 'name', 'account_type', 'bank_name', 'balance' ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        balance = form.cleaned_data.get('initial_balance')

        form.instance.initial_balance = self.money_field('balance', form)
        form.instance.balance = self.money_field('balance', form)

        return super().form_valid(form)

class ProductCreateView(CustomMixin, CreateView):
    model = Product
    success_url = '/'
    fields = [ 'name', 'account', 'product_type', 'price' ]

    def form_valid(self, form):
        account_pk = form.cleaned_data.get('account').pk

        balance = Account.objects.filter(user = self.request.user, pk = account_pk).values('balance')[0]['balance']
        price = self.money_field('price', form)

        new_balance = int(balance) - int(price)

        form.instance.user = self.request.user
        form.instance.price = self.money_field('price', form)
        Account.objects.filter(user = self.request.user, pk = account_pk).update(balance=new_balance)

        return super().form_valid(form)

class AccountListView(ListView):
    model = Account
    context_object_name = 'accounts'
    paginate_by = 20

class ProductListView(CustomMixin, ListView):
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total'] = self.field_sum(Product.objects.filter(user = self.request.user), 'price')

        return context
    