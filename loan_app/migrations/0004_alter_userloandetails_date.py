# Generated by Django 3.2.5 on 2021-08-12 14:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0003_alter_userloandetails_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userloandetails',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 8, 12, 14, 20, 11, 69759, tzinfo=utc)),
        ),
    ]
