# Generated by Django 4.1.7 on 2023-03-27 09:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_remove_profile_status'),
        ('customer', '0017_rename_paymentdetails_purchasedetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='productname',
            new_name='product',
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('user', 'product')},
        ),
    ]
