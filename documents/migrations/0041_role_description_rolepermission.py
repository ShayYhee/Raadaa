# Generated by Django 4.2.21 on 2025-07-01 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('documents', '0040_alter_task_documents'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='RolePermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.permission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.role')),
            ],
            options={
                'unique_together': {('role', 'permission')},
            },
        ),
    ]
