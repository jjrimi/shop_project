# Generated by Django 4.2.9 on 2024-02-16 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]