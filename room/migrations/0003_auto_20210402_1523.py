# Generated by Django 3.1.7 on 2021-04-02 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_auto_20210402_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='bookroom',
            name='checkin_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='bookroom',
            name='checkout_date',
            field=models.DateField(),
        ),
    ]
