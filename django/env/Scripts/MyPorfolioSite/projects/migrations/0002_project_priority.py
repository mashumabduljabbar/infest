# Generated by Django 3.0.3 on 2020-07-23 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]