# Generated by Django 4.0.4 on 2022-05-29 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Address_type',
            field=models.CharField(choices=[('HOME', 'HOME'), ('OFFICE', 'OFFICE'), ('OTHERS', 'OTHERS')], default='HOME', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserAddress',
        ),
    ]