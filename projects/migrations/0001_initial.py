# Generated by Django 3.2.9 on 2022-01-19 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image1', models.ImageField(upload_to='projects/%Y/%m/%d/')),
                ('image2', models.ImageField(upload_to='projects_sub/%Y/%m/%d/')),
                ('estimate_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('commencement_date', models.DateField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.projectcategory')),
            ],
        ),
    ]