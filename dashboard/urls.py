from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_account', login_required(views.AccountCreateView.as_view()), name='new-account'),
    path('new_product', login_required(views.ProductCreateView.as_view()), name='new-product'),
]
