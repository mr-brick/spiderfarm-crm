# Generated by Django 2.2.3 on 2019-08-09 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiderfarm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zonefragment',
            name='imported',
            field=models.BooleanField(default=False, verbose_name='Imported'),
        ),
    ]