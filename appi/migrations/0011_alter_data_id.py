# Generated by Django 3.2.4 on 2021-07-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appi', '0010_alter_data_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]