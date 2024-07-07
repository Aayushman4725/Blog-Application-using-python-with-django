# Generated by Django 5.0.6 on 2024-06-26 13:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0006_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='about',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='profile_picture',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(default='default.jpg', upload_to='images/profile_picture')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),
                ('about', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
