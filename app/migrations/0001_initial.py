# Generated by Django 3.2.7 on 2021-09-08 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVMaster',
            fields=[
                ('CsvID', models.AutoField(primary_key=True, serialize=False)),
                ('CsvName', models.FileField(max_length=255, upload_to='')),
            ],
        ),
    ]
