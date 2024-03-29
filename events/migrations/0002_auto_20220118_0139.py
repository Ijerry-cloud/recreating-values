# Generated by Django 3.2.9 on 2022-01-18 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='main_image',
            field=models.ImageField(blank=True, upload_to='main_events/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='event',
            name='sub_image',
            field=models.ImageField(blank=True, upload_to='sub_image/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='event',
            name='sub_image2',
            field=models.ImageField(blank=True, upload_to='sub_image2/%Y/%m/%d/'),
        ),
    ]
