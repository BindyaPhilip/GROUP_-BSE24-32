# Generated by Django 4.1.1 on 2022-09-29 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cakestore', '0017_rename_cart_id_cartitem_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cakestore.cart'),
        ),
    ]
