# Generated by Django 2.2.3 on 2019-08-08 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='bank_name',
            field=models.CharField(blank=True, choices=[('SA', 'Santander'), ('CX', 'Caixa'), ('BA', 'Bradesco'), ('NU', 'Nu Bank'), ('MV', 'Meal Valcher'), ('FV', 'Food Valcher')], max_length=10, null=True),
        ),
    ]