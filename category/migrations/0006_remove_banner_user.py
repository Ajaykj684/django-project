# Generated by Django 4.0.4 on 2022-06-16 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_banner_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='user',
        ),
    ]
