# Generated by Django 3.2 on 2021-04-18 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='locations',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Updated at'),
        ),
    ]
