# Generated by Django 3.2.9 on 2021-11-03 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='first_name',
        ),
    ]
