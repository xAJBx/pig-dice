# Generated by Django 3.2.6 on 2021-08-13 01:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
