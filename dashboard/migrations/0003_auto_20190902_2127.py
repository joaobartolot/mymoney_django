# Generated by Django 2.2.3 on 2019-09-02 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20190819_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='card_name',
            field=models.CharField(choices=[('VR', 'Vale Refeição'), ('VA', 'Vale Alimentação'), ('TR', 'Ticket Refeição'), ('TA', 'Ticket Alimentação'), ('AR', 'Alelo Refeição'), ('AA', 'Alelo Alimentação')], default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='bank_name',
            field=models.CharField(choices=[('SA', 'Santander'), ('CX', 'Caixa'), ('BA', 'Bradesco'), ('BB', 'Banco do Brasil'), ('IT', 'Itaú'), ('OR', 'Original'), ('CB', 'City Bank'), ('NU', 'Nu Bank')], default=None, max_length=10, null=True),
        ),
    ]
