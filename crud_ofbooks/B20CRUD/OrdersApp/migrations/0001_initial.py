# Generated by Django 3.2.6 on 2022-01-24 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.CharField(choices=[('Amazon', 'Amazon'), ('Flipkart', 'Flipkart'), ('Myntra', 'MYntra'), ('Ebay', 'Ebay')], max_length=32)),
                ('product', models.CharField(max_length=32)),
                ('qty', models.IntegerField()),
                ('price', models.FloatField()),
                ('is_paid', models.BooleanField()),
            ],
        ),
    ]
