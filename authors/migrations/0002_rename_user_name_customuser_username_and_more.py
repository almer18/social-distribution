# Generated by Django 5.0.2 on 2024-02-22 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='user_name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
