# Generated by Django 4.1.1 on 2022-09-29 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakestore', '0013_remove_cart_amount_remove_cart_name_cart_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='total_ordering',
            field=models.IntegerField(default=0),
        ),
    ]
