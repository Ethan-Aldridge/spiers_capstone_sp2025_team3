# Generated by Django 5.1.6 on 2025-02-23 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='battery',
            name='test_field',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
