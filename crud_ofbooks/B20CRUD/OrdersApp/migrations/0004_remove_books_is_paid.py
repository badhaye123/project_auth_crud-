# Generated by Django 3.2.6 on 2022-06-12 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrdersApp', '0003_rename_qty_books_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='is_paid',
        ),
    ]