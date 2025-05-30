# Generated by Django 4.2.20 on 2025-03-24 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0004_alter_battery_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarehouseA',
            fields=[
                ('serial_num', models.IntegerField(primary_key=True, serialize=False)),
                ('part_num', models.IntegerField()),
                ('item_type', models.CharField(max_length=60)),
                ('user_ID', models.CharField(max_length=80)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('madlibs', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseB',
            fields=[
                ('serial_num', models.IntegerField(primary_key=True, serialize=False)),
                ('part_num', models.IntegerField()),
                ('item_type', models.CharField(max_length=60)),
                ('user_ID', models.CharField(max_length=80)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('madlibs', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseC',
            fields=[
                ('serial_num', models.IntegerField(primary_key=True, serialize=False)),
                ('part_num', models.IntegerField()),
                ('item_type', models.CharField(max_length=60)),
                ('user_ID', models.CharField(max_length=80)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('madlibs', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
