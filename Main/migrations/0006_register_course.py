# Generated by Django 3.0.4 on 2020-09-21 16:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='Course',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
