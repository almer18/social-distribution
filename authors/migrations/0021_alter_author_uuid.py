# Generated by Django 5.0.2 on 2024-02-26 10:37

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0020_alter_author_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='uuid',
            field=models.CharField(default=uuid.UUID('78af8b6c-14fb-487b-b5a0-d54eaa02967e'), editable=False, max_length=50, unique=True),
        ),
    ]
