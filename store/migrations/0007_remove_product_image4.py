# Generated by Django 4.0.4 on 2022-05-31 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_images_product_image1_product_image2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image4',
        ),
    ]
