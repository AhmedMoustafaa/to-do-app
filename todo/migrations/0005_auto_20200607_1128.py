# Generated by Django 3.0.7 on 2020-06-07 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20200607_0715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='author',
        ),
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
