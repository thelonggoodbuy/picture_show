# Generated by Django 3.2.9 on 2021-12-01 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='cover',
            field=models.ImageField(upload_to='covers/'),
        ),
    ]
