# Generated by Django 2.2.3 on 2019-10-13 12:54

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('spiderfarm', '0011_auto_20191004_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertIssuerTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Certificate issuer',
                'verbose_name_plural': 'Certificate issuers',
            },
        ),
        migrations.RemoveField(
            model_name='domain',
            name='ssl_issuer_name',
        ),
        migrations.CreateModel(
            name='TaggedCertIssuers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spiderfarm_taggedcertissuers_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cert_issuer', to='spiderfarm.CertIssuerTag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='domain',
            name='ssl_issuer_name',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='spiderfarm.TaggedCertIssuers', to='spiderfarm.CertIssuerTag', verbose_name='SSL issuer'),
        ),
    ]
