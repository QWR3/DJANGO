# Generated by Django 3.2.7 on 2021-09-18 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0002_auto_20210918_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars'),
        ),
    ]