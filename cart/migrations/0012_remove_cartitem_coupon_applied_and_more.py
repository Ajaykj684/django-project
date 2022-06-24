# Generated by Django 4.0.4 on 2022-06-09 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_alter_cartitem_final_offer_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='coupon_applied',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='final_offer_price',
        ),
        migrations.AddField(
            model_name='carts',
            name='coupon_applied',
            field=models.CharField(blank=True, default=0, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='carts',
            name='final_offer_price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
