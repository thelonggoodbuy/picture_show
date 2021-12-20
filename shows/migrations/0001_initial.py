# Generated by Django 3.2.7 on 2021-10-03 11:56

import address.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0003_auto_20200830_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('cover', models.ImageField(blank=True, upload_to='covers/')),
                ('address', address.models.AddressField(blank='True', null='True', on_delete=django.db.models.deletion.SET_NULL, to='address.address')),
            ],
        ),
    ]
