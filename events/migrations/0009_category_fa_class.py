# Generated by Django 3.2.9 on 2022-02-14 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20220213_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='fa_class',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]