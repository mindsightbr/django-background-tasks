# Generated by Django 2.2 on 2020-01-30 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background_task', '0002_auto_20170927_1109'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['priority', 'run_at'], name='background__priorit_7a172d_idx'),
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['-priority', 'run_at'], name='background__priorit_44ffd0_idx'),
        ),
    ]
