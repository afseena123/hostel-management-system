# Generated by Django 5.0 on 2023-12-08 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosteldetails', '0003_beddetails_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
