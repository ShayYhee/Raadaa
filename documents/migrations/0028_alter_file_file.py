# Generated by Django 4.2.21 on 2025-06-18 13:58

from django.db import migrations, models
import documents.models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0027_alter_file_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=documents.models.upload_to_folder),
        ),
    ]
