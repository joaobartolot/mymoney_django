from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# TODO (Account):
#   - Account types should be a model

class Account(models.Model):
    """
    Account entity:
        Accounts attributes:
            - card name
            - account type (current, salary, savings, food voucher, meal voucher)
            - bank name
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

    BANKS_NAME = (
        ('SA', 'Santander'),
        ('CX', 'Caixa'),
        ('BA', 'Bradesco'),
        ('NU', 'Nu Bank'),
        ('MV', 'Meal Valcher'),
        ('FV', 'Food Valcher'),
    )

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    account_name = models.CharField(max_length = 100)
    account_type = models.CharField(choices = ACCOUNT_TYPES, max_length=10)
    bank_name = models.CharField(choices = BANKS_NAME, max_length=10, null=True, blank=True)
    balance = models.IntegerField()

    def __str__(self):
        return f'{self.account_name} ({self.bank_name}): {self.balance}'

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