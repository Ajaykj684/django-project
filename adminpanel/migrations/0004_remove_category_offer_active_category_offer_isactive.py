# Generated by Django 4.0.4 on 2022-06-12 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0003_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category_offer',
            name='active',
        ),
        migrations.AddField(
            model_name='category_offer',
            name='isactive',
            field=models.BooleanField(default=True),
        ),
    ]
