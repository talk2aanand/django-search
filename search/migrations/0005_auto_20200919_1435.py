# Generated by Django 2.1.15 on 2020-09-19 14:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20200919_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]