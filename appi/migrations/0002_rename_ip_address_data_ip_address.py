# Generated by Django 3.2.4 on 2021-07-12 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='ip_Address',
            new_name='ip_address',
        ),
    ]
