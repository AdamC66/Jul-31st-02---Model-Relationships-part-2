# Generated by Django 2.2.3 on 2019-07-31 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinook', '0004_auto_20190731_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='media_type',
            field=models.ManyToManyField(related_name='genres', through='chinook.Track', to='chinook.MediaType'),
        ),
    ]