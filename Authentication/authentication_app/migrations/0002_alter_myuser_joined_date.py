# Generated by Django 4.1.2 on 2022-10-06 08:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myuser",
            name="joined_date",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2022, 10, 6, 8, 8, 4, 293464)
            ),
        ),
    ]
