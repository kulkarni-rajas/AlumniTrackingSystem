# Generated by Django 3.0.4 on 2020-07-24 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20200715_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationtype',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='donation_images/'),
        ),
    ]
