# Generated by Django 4.0.4 on 2022-06-07 08:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_carts_carts_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(max_length=30, unique=True)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-valid_to'],
            },
        ),
    ]