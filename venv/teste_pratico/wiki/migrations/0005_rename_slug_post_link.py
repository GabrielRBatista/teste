# Generated by Django 3.2.9 on 2021-11-18 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_auto_20211118_1207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='slug',
            new_name='link',
        ),
    ]
