# Generated by Django 3.1.7 on 2021-04-09 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0008_auto_20210409_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookroom',
            name='has_checkedin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookroom',
            name='has_checkedout',
            field=models.BooleanField(default=False),
        ),
    ]