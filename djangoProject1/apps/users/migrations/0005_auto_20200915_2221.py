# Generated by Django 3.1.1 on 2020-09-15 19:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200915_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('bcfd5ac3-4163-424d-be41-bf6d4f92abcd'), editable=False, primary_key=True, serialize=False),
        ),
    ]
