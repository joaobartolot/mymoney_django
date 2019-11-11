from django.shortcuts import render
from rest_framework.generics import ListAPIView

from dashboard.models import Account
from .serializers import AccountSerializer

# Create your views here.

class AccountListView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer