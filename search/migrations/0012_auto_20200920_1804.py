# Generated by Django 2.1.15 on 2020-09-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0011_submit_total_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='date',
            field=models.DateField(auto_created=True, null=True),
        ),
        migrations.AddField(
            model_name='url',
            name='links',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
