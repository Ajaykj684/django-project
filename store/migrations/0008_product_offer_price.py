# Generated by Django 4.0.4 on 2022-06-06 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_product_image4'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offer_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
