# Generated by Django 3.0.4 on 2020-12-22 05:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_project_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
