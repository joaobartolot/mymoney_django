# Generated by Django 2.2.3 on 2019-08-09 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20190807_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.CharField(max_length=1000000),
        ),
    ]
