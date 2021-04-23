# Generated by Django 3.1.7 on 2021-04-09 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookroom',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='room.roominfo'),
            preserve_default=False,
        ),
    ]
