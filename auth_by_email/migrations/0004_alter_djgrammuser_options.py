# Generated by Django 3.2.9 on 2021-12-04 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_by_email', '0003_alter_djgrammuser_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='djgrammuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]