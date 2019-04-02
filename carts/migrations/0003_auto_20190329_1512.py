# Generated by Django 2.1.7 on 2019-03-29 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cart_subtotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=100),
        ),
    ]
