# Generated by Django 4.0.4 on 2022-06-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='is_applied',
            field=models.BooleanField(default=False),
        ),
    ]