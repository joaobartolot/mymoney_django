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
    name = models.CharField(max_length = 100)
    account_type = models.CharField(choices = ACCOUNT_TYPES, max_length=10)
    bank_name = models.CharField(choices = BANKS_NAME, max_length=10, null=True, blank=True)
    initial_balance = models.CharField(max_length = 100000000000)
    balance = models.CharField(max_length = 100000000000)

    def __str__(self):
        return f'{self.name}: R$ {self.balance[:-2]},{self.balance[-2:]}'

    @property
    def account_expenses(self):
        return Expense.objects.filter(account = self.pk)

    @property
    def total_expenses(self):
        '''
            Expenses per account
        '''
        product_filter = Expense.objects.filter(account = self.pk)

        total = 0

        for product in product_filter:
            total += int(product.price)

        total = str(total)

        if total == '0':
            total = '000'

        return f'R$ - {total[:-2]},{total[-2:]}'

# TODO (Expense):
#   - Expense types should be a model

class Expense(models.Model):
    """
    Expense entity:
        Expense attributes:
            - type (food, tech, ...)
            - name
            - price

        Expense relationships:
            - User (foreign key)
            - Account (foreign key)
    """

    EXPENSE_TYPES = ( 
        ('F', 'Food'),
        ('S', 'Snack'),
        ('B', 'Bill'),
        ('C', 'Clothing'),
  )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    expense_type = models.CharField(choices = EXPENSE_TYPES, max_length=10)
    price = models.CharField(max_length = 100000000000)
