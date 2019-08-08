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
        'account_name',
        'account_type',
        'bank_name',
        'balance'
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)