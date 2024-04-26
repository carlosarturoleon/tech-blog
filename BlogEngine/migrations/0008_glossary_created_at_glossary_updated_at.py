# Generated by Django 5.0 on 2024-04-26 02:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogEngine', '0007_glossary_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='glossary',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='glossary',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
