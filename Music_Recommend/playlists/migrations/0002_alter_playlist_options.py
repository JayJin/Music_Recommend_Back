# Generated by Django 4.1.3 on 2022-11-03 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playlist',
            options={'ordering': ['-created_at']},
        ),
    ]
