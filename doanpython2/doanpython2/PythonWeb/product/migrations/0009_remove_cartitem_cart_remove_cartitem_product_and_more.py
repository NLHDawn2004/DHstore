# Generated by Django 5.0.3 on 2024-03-20 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_endow_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
