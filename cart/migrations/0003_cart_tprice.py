# Generated by Django 4.0 on 2023-04-12 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cart_product_alter_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tprice',
            field=models.DecimalField(decimal_places=2, default=19, max_digits=10),
            preserve_default=False,
        ),
    ]