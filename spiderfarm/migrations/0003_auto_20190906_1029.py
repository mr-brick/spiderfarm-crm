# Generated by Django 2.2.3 on 2019-09-06 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiderfarm', '0002_zonefragment_imported'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='geoip_error',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='GeoIP error message'),
        ),
        migrations.AddField(
            model_name='domain',
            name='ssl_error',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='SSL error message'),
        ),
        migrations.AddField(
            model_name='domain',
            name='whois_error',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='WHOIS error message'),
        ),
    ]
