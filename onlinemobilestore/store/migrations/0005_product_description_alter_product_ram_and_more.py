# Generated by Django 4.1.7 on 2023-03-30 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_ram_alter_product_rom'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ram',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='rom',
            field=models.IntegerField(),
        ),
    ]
