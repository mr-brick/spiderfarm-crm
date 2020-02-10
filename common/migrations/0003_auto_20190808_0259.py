# Generated by Django 2.2.3 on 2019-08-08 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
        ('events', '0001_initial'),
        ('tasks', '0001_initial'),
        ('cases', '0002_auto_20190808_0259'),
        ('common', '0002_auto_20190808_0259'),
        ('leads', '0001_initial'),
        ('opportunity', '0001_initial'),
        ('invoices', '0001_initial'),
        ('accounts', '0003_auto_20190808_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='lead',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leads_comments', to='leads.Lead'),
        ),
        migrations.AddField(
            model_name='comment',
            name='opportunity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opportunity_comments', to='opportunity.Opportunity'),
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks_comments', to='tasks.Task'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attachments',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_attachment', to='accounts.Account'),
        ),
        migrations.AddField(
            model_name='attachments',
            name='case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_attachment', to='cases.Case'),
        ),
        migrations.AddField(
            model_name='attachments',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_attachment', to='contacts.Contact'),
        ),
        migrations.AddField(
            model_name='attachments',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attachment_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attachments',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events_attachment', to='events.Event'),
        ),
        migrations.AddField(
            model_name='attachments',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_attachment', to='invoices.Invoice'),
        ),
        migrations.AddField(
            model_name='attachments',
            name='lead',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lead_attachment', to='leads.Lead'),
        ),
        migrations.AddField(
            model_name='attachments',
            name='opportunity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opportunity_attachment', to='opportunity.Opportunity'),
        ),
        migrations.AddField(
            model_name='attachments',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks_attachment', to='tasks.Task'),
        ),
        migrations.AddField(
            model_name='apisettings',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='settings_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='apisettings',
            name='lead_assigned_to',
            field=models.ManyToManyField(related_name='lead_assignee_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='apisettings',
            name='tags',
            field=models.ManyToManyField(blank=True, to='accounts.Tags'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]