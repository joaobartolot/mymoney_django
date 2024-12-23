# Generated by Django 2.2.3 on 2019-09-02 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20190902_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='bank_name',
            field=models.CharField(blank=True, choices=[('SA', 'Santander'), ('CX', 'Caixa'), ('BA', 'Bradesco'), ('BB', 'Banco do Brasil'), ('IT', 'Itaú'), ('OR', 'Original'), ('CB', 'City Bank'), ('NU', 'Nu Bank')], default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='card_name',
            field=models.CharField(blank=True, choices=[('VR', 'Vale Refeição'), ('VA', 'Vale Alimentação'), ('TR', 'Ticket Refeição'), ('TA', 'Ticket Alimentação'), ('AR', 'Alelo Refeição'), ('AA', 'Alelo Alimentação')], default=None, max_length=10, null=True),
        ),
    ]
