# Generated by Django 3.2.7 on 2021-09-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvmaster',
            name='CsvName',
            field=models.FileField(upload_to=''),
        ),
    ]
