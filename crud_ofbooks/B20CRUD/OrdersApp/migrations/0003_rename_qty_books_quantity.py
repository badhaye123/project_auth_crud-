# Generated by Django 3.2.6 on 2022-02-20 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrdersApp', '0002_auto_20220130_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='qty',
            new_name='quantity',
        ),
    ]
