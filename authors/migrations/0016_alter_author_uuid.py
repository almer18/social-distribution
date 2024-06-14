# Generated by Django 5.0.2 on 2024-02-26 02:03

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0015_author_uuid_alter_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='uuid',
            field=models.CharField(default=uuid.UUID('affcc7f8-3dda-4b4c-86c3-269f844b21a6'), editable=False, max_length=50, unique=True),
        ),
    ]