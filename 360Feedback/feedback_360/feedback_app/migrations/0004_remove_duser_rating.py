# Generated by Django 3.1.7 on 2021-10-20 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_app', '0003_auto_20211020_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duser',
            name='rating',
        ),
    ]
