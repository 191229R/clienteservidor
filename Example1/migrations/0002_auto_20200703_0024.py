# Generated by Django 2.2.1 on 2020-07-03 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Example1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='example1',
            name='curp',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='example1',
            name='direccion',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='example1',
            name='edad',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
