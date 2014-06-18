# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20140617_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='total',
            field=models.IntegerField(default=datetime.date(2014, 6, 18)),
            preserve_default=False,
        ),
    ]
