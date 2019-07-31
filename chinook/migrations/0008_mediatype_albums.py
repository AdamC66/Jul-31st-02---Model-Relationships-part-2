# Generated by Django 2.2.3 on 2019-07-31 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinook', '0007_genre_albums'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediatype',
            name='albums',
            field=models.ManyToManyField(related_name='media_type', to='chinook.Album'),
        ),
    ]
