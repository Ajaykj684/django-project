# Generated by Django 4.0.4 on 2022-06-07 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_carts_coupon_applied'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carts',
            name='coupon_applied',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='coupon_applied',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
