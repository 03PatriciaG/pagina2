# Generated by Django 3.1.7 on 2021-03-12 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210311_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='descripcion',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
