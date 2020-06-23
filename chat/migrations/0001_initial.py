# Generated by Django 3.0.4 on 2020-06-23 13:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.TextField()),
                ('date_posted', models.DateTimeField(default=datetime.datetime.now)),
                ('parent_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Alumni')),
            ],
        ),
    ]
