# Generated by Django 4.2.21 on 2025-07-02 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0002_tenantapplication_tenant_admin_tenant_created_by_and_more'),
        ('documents', '0042_role_tenant_rolepermission_tenant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tenant',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tenants.tenant'),
        ),
    ]
