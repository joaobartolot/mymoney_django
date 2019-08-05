from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# TODO (Account):
#   - Account types should be a model

class Account(models.Model):
    """
    Account entity:
        Accounts attributes:
            - account type (current, salary, savings, food voucher, meal voucher)
            - balace
        Accounts relationships:
            - User
    """

    ACCOUNT_TYPES = ( 
        ('CA', 'Current Account'),
        ('SL', 'Salary Account'),
        ('SA', 'Savings Account'),
        ('FV', 'Food Voucher'),
        ('MV', 'Meal Voucher'),
        ('W', 'Wallet'),
  )

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    account_type = models.CharField(choices = ACCOUNT_TYPES, max_length=10)
    balance = models.IntegerField()

# TODO (Product):
#   - Product types should be a model to

class Product(models.Model):
    """
    Product entity:
        Product attributes:
            - type (food, tech, ...)
            - name
            - price

        Products relationships:
            - User (foreign key)
            - Account (foreign key)
    """

    PRODUCT_TYPES = ( 
        ('F', 'Food'),
        ('S', 'Snack'),
        ('B', 'Bill'),
        ('C', 'Clothing'),
  )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    product_type = models.CharField(choices = PRODUCT_TYPES, max_length=10)
    price = models.IntegerField()