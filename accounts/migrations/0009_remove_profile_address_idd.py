# Generated by Django 4.0.4 on 2022-06-04 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_profile_address_idd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Address_idd',
        ),
    ]