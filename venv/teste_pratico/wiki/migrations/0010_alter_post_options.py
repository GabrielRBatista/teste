# Generated by Django 3.2.9 on 2021-11-19 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0009_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-updated']},
        ),
    ]
