# Generated by Django 4.2.21 on 2025-07-01 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0002_tenantapplication_tenant_admin_tenant_created_by_and_more'),
        ('documents', '0041_role_description_rolepermission'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='tenant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tenants.tenant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rolepermission',
            name='tenant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tenants.tenant'),
            preserve_default=False,
        ),
    ]
