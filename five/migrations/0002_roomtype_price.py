# Generated by Django 3.1 on 2020-09-22 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('five', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='price',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
