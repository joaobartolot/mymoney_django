from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_account/', login_required(views.AccountCreateView.as_view()), name='new-account'),
    path('accounts/', login_required(views.AccountListView.as_view()), name='accounts'),
    path('account/<int:pk>/', login_required(views.AccountDetailView.as_view()), name='account-detail'),
    path('account/<int:pk>/delete/', login_required(views.AccountDeleteView.as_view()), name='account-delete'),
    path('account/detail/<int:pk>/delete/', login_required(views.AccountDetailDeleteView.as_view()), name='account-detail-delete'),
    path('account/<int:pk>/update/', login_required(views.AccountUpdateView.as_view()), name='account-update'),
    path('account/detail/<int:pk>/update/', login_required(views.AccountUpdateDetailView.as_view()), name='account-detail-update'),
    path('new_expense/', login_required(views.ExpenseCreateView.as_view()), name='new-expense'),
    path('expenses/', login_required(views.ExpenseListView.as_view()), name='expenses'),
]
