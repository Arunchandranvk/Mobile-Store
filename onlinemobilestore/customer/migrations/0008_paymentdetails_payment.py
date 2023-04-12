# Generated by Django 4.1.7 on 2023-03-25 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_profile_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0007_rename_product_cart_productname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paymentdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('totalprice', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_details', to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=100)),
                ('acholdername', models.CharField(max_length=100)),
                ('accno', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_payment', to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_payment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]