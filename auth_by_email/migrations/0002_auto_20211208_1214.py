# Generated by Django 3.2.9 on 2021-12-08 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_by_email', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='follower',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='following',
            old_name='following',
            new_name='user',
        ),
    ]