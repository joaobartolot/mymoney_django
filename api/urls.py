from django.urls import path

from .views import AccountListView

urlpatterns = [
    path('account_list/', AccountListView.as_view())
]
