# Generated by Django 3.2.21 on 2023-10-01 10:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_backend', '0003_users_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logs',
            old_name='descrpiption',
            new_name='message',
        ),
        migrations.AddField(
            model_name='logs',
            name='level_event',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logs',
            name='more_information',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
