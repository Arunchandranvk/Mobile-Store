# Generated by Django 4.1.7 on 2023-03-25 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_cart_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product',
            new_name='productname',
        ),
    ]