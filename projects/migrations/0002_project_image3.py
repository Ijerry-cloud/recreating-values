# Generated by Django 3.2.9 on 2022-01-20 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image3',
            field=models.ImageField(blank=True, upload_to='projects_sub/%Y/%m/%d/'),
        ),
    ]