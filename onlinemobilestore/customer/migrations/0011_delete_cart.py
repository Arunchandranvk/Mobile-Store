# Generated by Django 4.1.7 on 2023-03-25 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_alter_cart_unique_together'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
