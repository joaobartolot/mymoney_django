# Generated by Django 2.2.3 on 2019-08-10 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20190809_2034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='account_name',
            new_name='name',
        ),
    ]