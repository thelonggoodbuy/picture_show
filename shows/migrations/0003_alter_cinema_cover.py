# Generated by Django 3.2.7 on 2021-09-23 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0002_cinema_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
