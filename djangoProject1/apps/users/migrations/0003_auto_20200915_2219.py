# Generated by Django 3.1.1 on 2020-09-15 19:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200915_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a2330834-b9a4-4246-832f-9a954b188389'), editable=False, primary_key=True, serialize=False),
        ),
    ]