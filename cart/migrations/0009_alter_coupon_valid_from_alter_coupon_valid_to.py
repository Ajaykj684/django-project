# Generated by Django 4.0.4 on 2022-06-08 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_remove_carts_coupon_applied_remove_carts_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='valid_from',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(null=True),
        ),
    ]