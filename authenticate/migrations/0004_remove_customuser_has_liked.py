# Generated by Django 5.0.6 on 2024-06-23 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_customuser_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='has_liked',
        ),
    ]
